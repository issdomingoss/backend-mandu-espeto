from flask import Flask, request
from flask.json import jsonify

from app.models.espeto_model import Espeto


def init_app(app: Flask):
    @app.get("/espetos")
    def get_all_espeto():
        espetos = Espeto.get_all_espeto()
        return jsonify(espetos), 200

    @app.post("/espetos")
    def create_espeto():
        data = request.json

        output = Espeto.create_espeto(data)

        return output

    @app.delete("/espetos/<int:espeto_id>")
    def delete_espeto(espeto_id):
        del_espeto = Espeto.delete_espeto(espeto_id)
        return del_espeto
