from flask_restful import Resource
from api.extensions import db, custom_response

class Users(Resource):

    def get(self):
        users = [user for user in db.users.find({}, {'_id': 0})]
        return custom_response(payload=users)

class User(Resource):
    def get(self, id):
        user = db.users.find_one({'uid': id}, {'_id': 0})
        if not user:
            return custom_response(success=False, error='id inexistente')
        messages = [msg for msg in db.messages.find({
                'sender': id
                }, {'_id': 0})]

        response = {
            'user': user,
            'messages': messages
        }
        return custom_response(payload=response)
