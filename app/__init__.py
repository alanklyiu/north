from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Local imports
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
# The default message flashed is "Please log in to access this page."
#login.login_message = "You must be logged in to access this page."

# I think contents inside parentheses are parsed as Python literals and
# passed as arguments and keyword arguments to the create_app function
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    #from . import models

    from .errors import errors_bp
    app.register_blueprint(errors_bp)

    #from .admin import admin_bp
    #app.register_blueprint(admin_bp, url_prefix='/admin')

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .home import home_bp
    app.register_blueprint(home_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    # returns the application instance
    return app