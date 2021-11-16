from flask import Flask
from app.routes import espeto_route


def create_app():
    app = Flask(__name__)
    espeto_route.init_app(app)
    return app
