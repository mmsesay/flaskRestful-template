from flask import Flask
from flask_restful import Api
from routes.router import initialize_routes


def init_app():
    app = Flask(__name__)
    api = Api(app)
    initialize_routes(api)

    return app
