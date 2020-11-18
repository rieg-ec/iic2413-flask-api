from marshmallow import Schema, fields


class TextSearchPOST(Schema):
    desired = fields.List(fields.String())
    required = fields.List(fields.String())
    forbidden = fields.List(fields.String())
    user_id = fields.Integer(data_key='userId')
