from flask_restful import Resource
from flask import request, Response
from api.extensions import db
from api.schemas.messages import MessagesPOSTSchema


class Messages(Resource):

    def get(self):
        if not request.args:
            return [i for i in db.messages.find({}, {'_id': 0})]

        elif all(arg in list(request.args.keys()) for arg in ['id1', 'id2']):
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

            return {'result': [messages_id1, messages_id2]}

        return "Hubo un error", 400

    def post(self):
        body = request.get_json()
        errors = MessagesPOSTSchema().validate(body)
        if errors:
            return errors, 400

        new_id = int(db.messages.find({}, {'_id': 0, 'mid': 1}).sort(
            [('mid', -1)]).limit(1)[0]['mid']) + 1

        body['mid'] = new_id

        db.messages.insert(body)

        return Response(status=204)


class Message(Resource):

    def get(self, id):
        return db.messages.find_one({'mid': id}, {'_id': 0})


class DeleteMessage(Resource):
    
    def delete(self, id):
        db.messages.delete_one({'mid': id})
        return Response(status=204)
