from flask_restful import Resource
from flask import jsonify


class Users(Resource):
    def get(self, id):
        return {'hola': 'hola' + id}


class User(Resource):
    def get(self, id):
        pass
