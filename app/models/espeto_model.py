import pymongo
from flask import jsonify

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['mandu']


class Espeto:
    def __init__(self, name_espeto: str, type_flavors: str, price: int):
        self.name_espeto = name_espeto
        self.type_flavors = 'None'
        self.price = price

    def get_all_espeto():
        espeto_list = list(db.espeto.find())

        for espeto in espeto_list:
            del espeto['_id']

        return espeto_list

    def create_espeto(self):
        new_espeto = self

        try:
            field_allowed = ['name_espeto', 'type_flavors', 'price']

            for key in new_espeto:
                if key not in field_allowed:
                    return {'Error': "Campo Inválido"}, 409

            get_espeto = list(db.espeto.find())

            if len(get_espeto) == 0:
                new_espeto['id'] = 1
            else:
                new_espeto['id'] = get_espeto[-1]['id'] + 1

            db.espeto.insert_one(new_espeto)

            del new_espeto['_id']

            return jsonify(new_espeto), 201

        except TypeError as e:
            return e

    @staticmethod
    def delete_espeto(espeto_id):
        try:
            del_espeto = list(db.espeto.find({'id': int(espeto_id)}))

            if len(del_espeto) == 0:
                return {'Error': 'Produto Indisponível ou deletado!'}, 409
            db.espeto.delete_one(del_espeto[0])

            del del_espeto[0]['_id']

            return jsonify(del_espeto[0]), 200

        except TypeError as e:
            return e
