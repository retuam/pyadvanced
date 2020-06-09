from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    first_name = fields.String(required=True, validate=[validate.Length(min=1, max=16)])
    last_name = fields.String(validate=[validate.Length(max=32)])
    parent_name = fields.String(validate=[validate.Length(max=32)])
    telephone = fields.String(required=True, validate=[validate.Length(max=128)])
    email = fields.Email()
    address = fields.String(validate=[validate.Length(max=256)])
    comment = fields.String(validate=[validate.Length(max=4096)])
    status = fields.Integer(dump_only=True, default=0)
    chat_id = fields.Integer(dump_only=True, required=True)
