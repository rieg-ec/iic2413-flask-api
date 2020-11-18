from flask_restful import Resource
from flask import request
from api.extensions import db
from api.schemas.text_search import TextSearchPOST
from .utils import build_text_search_pipeline, filter_forbidden


class TextSearch(Resource):
    def post(self):
        body = request.get_json()
        errors = TextSearchPOST().validate(body)
        if errors:
            return errors, 400

        pipeline = build_text_search_pipeline(body)

        cursor = db.messages.aggregate(pipeline)

        if 'required' not in body.keys() and 'forbidden' in body.keys():
            result = filter_forbidden(cursor, body['forbidden'])
        else:
            result = [document for document in cursor]

        return {'result': result}
