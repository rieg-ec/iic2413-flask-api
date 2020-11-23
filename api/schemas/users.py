from marshmallow import Schema, fields, validate


class UsersPOSTSchema(Schema):
    message = fields.String(required=True)
    sender = fields.Integer(required=True)
    description = fields.String(required=True)
