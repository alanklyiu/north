from app import create_app
app = create_app()

# The run command of the flask script starts the development server.
# It replaces the Flask.run() method in most cases, and is recommended from
# Flask 0.11 onwards
#
#if __name__ == '__main__':
#    app.run()
#
# https://flask.palletsprojects.com/en/2.2.x/cli/
# Flask is told about the application by the --app option.
# If nothing is specified, the name "app" or "wsgi" is imported (as a ".py"
# file, or package), automatically detecting an app (app or application) or
# factory (create_app or make_app).