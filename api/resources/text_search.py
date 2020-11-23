from flask_restful import Resource
from flask import request
from .utils import (
    build_text_search_pipeline, filter_forbidden,
    forbidden_pipeline
)
from api.extensions import db, custom_response
from api.schemas.text_search import TextSearchPOST


class TextSearch(Resource):
    def get(self):
        body = request.get_json(silent=True)
        if not body:
            return custom_response(
                payload=[msg for msg in db.messages.find({}, {'_id': 0})]
            )

        errors = TextSearchPOST().validate(body)
        if errors:
            return custom_response(success=False, error=errors)

        pipeline = build_text_search_pipeline(body)
        cursor = db.messages.aggregate(pipeline)

        if (body.get('forbidden')
            and not body.get('required')
            and not body.get('desired')
            ):
            forbidden_cursor = db.messages.aggregate(forbidden_pipeline(body))
            collection = filter_forbidden(cursor, forbidden_cursor)

        else:
            collection = [document for document in cursor]

        return custom_response(payload=collection)
