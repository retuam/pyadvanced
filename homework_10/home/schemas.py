from marshmallow import Schema, fields, validate, validates, ValidationError


class CategorySchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True, validate=[validate.Length(min=3, max=256)])


class SubcategorySchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True, validate=[validate.Length(min=3, max=256)])
    category = fields.Nested(CategorySchema, required=True)


class ProductSchema(Schema):
    id = fields.String(dump_only=True)
    subcategory = fields.Nested(SubcategorySchema, required=True)
    title = fields.String(required=True, validate=[validate.Length(min=3, max=256)])
    body = fields.String(required=True, validate=[validate.Length(min=3, max=4096)])
    created = fields.DateTime(dump_only=True, required=True)
    views = fields.Integer(dump_only=True, default=0)
    qty = fields.Integer(dump_only=True, default=0)
    price = fields.Float(default=0)
    sale = fields.Boolean(default=True)
