from flask import render_template
#from flask_login import login_required

from . import home_bp


@home_bp.route('/')
@home_bp.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('home/index.html', title="Welcome", posts=posts)