from flask import flash, redirect, render_template, url_for, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_required, login_user, logout_user

from . import auth_bp
from .forms import LoginForm, SignupForm
from app import db
from app.models import User


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()
    """
    redirect returns a 302 header to the browser, with its Location header as
             the URL for its argument
    render_template returns a 200, with the template of its argument returned
                    as the content at that URL
    netloc = network location, which includes the domain itself (and subdomain
             if present), the port number, along with an optional credentials
             in the form of username:password, as per Section 3.1 of RFC 1738.
             Together it may take the form of username:password@example.com:80
    """
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home.index')
            return redirect(next_page)
        flash("Invalid email or password")
    return render_template('auth/login.html', title="Log in", form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully.")
    return redirect(url_for('home.index'))


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations! You can now log in.")
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', title="Sign up", form=form)