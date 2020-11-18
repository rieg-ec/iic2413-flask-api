from flask_restful import Resource
from flask import request
from .utils import (
    build_score, build_text_search_pipeline,
    filter_forbidden
)
from api.extensions import db
from api.schemas.text_search import TextSearchPOST


class TextSearch(Resource):
    def get(self):
        body = request.get_json()
        errors = TextSearchPOST().validate(body)
        if errors:
            return errors, 400

        pipeline = build_text_search_pipeline(body)
        cursor = db.messages.aggregate(pipeline)

        if 'required' not in body.keys() and 'forbidden' in body.keys():
            collection = filter_forbidden(cursor, body['forbidden'])
        else:
            collection = [document for document in cursor]

        if 'desired' in body.keys():
            build_score(collection, body['desired'])
            collection.sort(key=lambda x: x['score'], reverse=True)

        return collection
