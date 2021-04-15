from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'sdasdsdfasdf'

    from . import urlShort
    app.register_blueprint(urlShort.bp)

    return app
