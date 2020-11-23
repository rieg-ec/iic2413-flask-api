from flask_restful import Resource
from flask import request, Response
from api.extensions import db
from api.schemas.users import UsersPOSTSchema


class Users(Resource):

    def get(self):
        if not request.args:
            return [i for i in db.users.find({}, {'_id': 0})]

        elif all(arg in list(request.args.keys()) for arg in ['id1']):
            try:
                id1 = int(request.args['id1'])
            except ValueError:
                return 'id invalido'

            if not db.users.find_one({'uid': id1}):
                return 'id inexistente'

        return "Hubo un error", 400


class User(Resource):
    def get(self, id):
        messages_id1 = [i for i in db.messages.find({
                'sender': id
                }, {'_id': 0})]

        user_id1 = [i for i in db.users.find({'uid': id
                }, {'_id': 0})]

        return {'result': [user_id1, messages_id1]}
        
