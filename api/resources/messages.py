from flask_restful import Resource
from flask import request, Response
from marshmallow import ValidationError
from api.extensions import db
from api.schemas import messages


class Messages(Resource):
    def get(self):
        if len(request.args) == 0:
            messages = [i for i in db.messages.find({}, {'_id': 0})]
            return messages

        if request.args['id1'] and request.args['id2']:
            try:
                id1 = int(request.args['id1'])
                id2 = int(request.args['id2'])
            except ValueError:
                return 'ids invalidos'

            if not db.users.find_one({'uid': id1}) or\
                    not db.users.find_one({'uid': id2}):
                return 'ids inexistentes'

            messages_id1 = [i for i in db.messages.find({
                'sender': id1,
                'receptant': id2
                }, {'_id': 0})]

            messages_id2 = [i for i in db.messages.find({
                'sender': id2,
                'receptant': id1
                }, {'_id': 0})]

            return [messages_id1, messages_id2]

        return "Hubo un error :whale:", 400

    def post(self):
        body = request.get_json()
        errors = messages.ValidateMessagesSchema().validate(body)
        if errors:
            return errors, 400

        new_id = int(db.messages.find({}, {'_id': 0, 'mid': 1}).sort(
            [('mid', -1)]).limit(1)[0]['mid']) + 1

        body['mid'] = new_id
        db.messages.insert(messages.MessagesPOSTSchema().load(body))
        return Response(status=204)

class Message(Resource):
    def get(self, id):
        message = db.messages.find_one({'mid': id}, {'_id': 0})
        return message

    def delete(self, id):
        if not db.messages.find_one({'mid': id}):
            return 'mensaje inexistente'

        db.messages.delete_one({'mid': id})
        return Response(status=204)
