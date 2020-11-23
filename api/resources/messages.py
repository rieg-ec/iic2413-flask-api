from flask_restful import Resource
from flask import request, Response
from api.extensions import db
from api.schemas.messages import MessagesPOSTSchema
from .utils import custom_response

class Messages(Resource):

    def get(self):
        if not request.args:
            return custom_response(
                payload=[msg for msg in db.messages.find({}, {'_id': 0})]
            )

        try:
            id1 = int(request.args.get('id1'))
            id2 = int(request.args.get('id2'))

            if (not db.users.find_one({'uid': id1})
                or not db.users.find_one({'uid': id2})
                ):
                return custom_response(success=False, error='ids inexistentes')

            messages_id1 = [msg for msg in db.messages.find({
                'sender': id1,
                'receptant': id2
                }, {'_id': 0})]

            messages_id2 = [msg for msg in db.messages.find({
                'sender': id2,
                'receptant': id1
                }, {'_id': 0})]

            return custom_response(payload=[messages_id1, messages_id2])

        except ValueError:
            return custom_response(success=False, error='invalid url args')

        except Exception as e:
            return custom_response(success=False, error='hubo un error')


    def post(self):
        body = request.get_json(silent=True)
        if not body:
            return custom_response(success=False, error='empty body')

        errors = MessagesPOSTSchema().validate(body)
        if errors:
            return custom_response(success=False, error=errors)

        try:
            new_id = int(db.messages.find({}, {'_id': 0, 'mid': 1}).sort(
                [('mid', -1)]).limit(1)[0]['mid']) + 1

            body['mid'] = new_id

            msg = db.messages.insert(body)
            return custom_response(payload=f'mensaje con mid {new_id} creado')

        except Exception as e:
            return custom_response(success=False, error='hubo un error')


class Message(Resource):

    def get(self, id):
        message = db.messages.find_one({'mid': id}, {'_id': 0})
        if not message:
            return custom_response(success=False, error='id inexistente')

        return custom_response(payload=message)


class DeleteMessage(Resource):

    def delete(self, id):
        try:
            operation = db.messages.delete_one({'mid': id})
            if not operation.deleted_count:
                return custom_response(success=False, error='id inexistente')

            return custom_response(payload=f'mensaje con id {id} eliminado')

        except Exception as e:
            return custom_response(success=False, error='hubo un error')
