from marshmallow import Schema, fields, validate, INCLUDE

class MessagesPOSTSchema(Schema):
    message = fields.String(required=True)
    sender = fields.Integer(required=True)
    receptant = fields.Integer(required=True)
    lat = fields.Float(required=True,
        validate=validate.Range(min=-85.5, max=85.0))
    long = fields.Float(required=True,
        validate=validate.Range(min=-180, max=180))

    class Meta:
        unknown = INCLUDE

class ValidateMessagesSchema(MessagesPOSTSchema):
    date = fields.DateTime(format='%Y-%m-%d', required=True)
