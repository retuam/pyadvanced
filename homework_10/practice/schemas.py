from marshmallow import Schema, fields, validate, validates, ValidationError


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(min=1, max=128)])
    surname = fields.String(required=True, validate=[validate.Length(min=1, max=128)])
    post_qty = fields.Integer(dump_only=True, required=False, default=0)


class TagSchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True, validate=[validate.Length(min=3, max=256)])


class PostSchema(Schema):
    id = fields.String(dump_only=True)
    author = fields.Nested(AuthorSchema, required=True)
    title = fields.String(required=True, validate=[validate.Length(min=3, max=256)])
    body = fields.String(required=True, validate=[validate.Length(min=3, max=4096)])
    created = fields.DateTime(dump_only=True, required=True)
    views = fields.Integer(dump_only=True, default=0)
    tags = fields.List(fields.Nested(TagSchema, required=True))
