from flask_restful import Resource
from homework_10.home.models import *
from flask import request, jsonify
import json
from homework_10.home import schemas
from marshmallow import ValidationError


class CategoryResource(Resource):
    def get(self, id=None):
        if id:
            json_obj = schemas.CategorySchema().dumps(Category.objects(id=id).first())
        else:
            json_obj = schemas.CategorySchema(many=True).dumps(Category.objects.all())
        return jsonify(json.loads(json_obj))

    def post(self):
        json_data = json.dumps(request.json)
        try:
            res = schemas.CategorySchema().loads(json_data)
            Category.objects.create(**res)
            res = json.loads(schemas.CategorySchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, id):
        json_data = json.dumps(request.json)
        try:
            res = schemas.CategorySchema().loads(json_data)
            Category.objects(id=id).update(**res)
            data = Category.objects(id=id).first()
            json_obj = schemas.CategorySchema().dumps(data)
            res = jsonify(json.loads(json_obj))
        except ValidationError as err:
            res = err.messages
        return res

    def delete(self, id):
        data = Category.objects(id=id).delete()
        return jsonify(data)


class SubcategoryResource(Resource):
    def get(self, id=None):
        if id:
            json_obj = schemas.SubcategorySchema().dumps(Subcategory.objects(id=id).first())
        else:
            json_obj = schemas.SubcategorySchema(many=True).dumps(Subcategory.objects.all())
        return jsonify(json.loads(json_obj))

    def post(self):
        json_data = json.dumps(request.json)
        try:
            res = schemas.SubcategorySchema().loads(json_data)
            Subcategory.objects.create(**res)
            res = json.loads(schemas.SubcategorySchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, id):
        json_data = json.dumps(request.json)
        try:
            res = schemas.SubcategorySchema().loads(json_data)
            Subcategory.objects(id=id).update(**res)
            data = Subcategory.objects(id=id).first()
            json_obj = schemas.SubcategorySchema().dumps(data)
            res = jsonify(json.loads(json_obj))
        except ValidationError as err:
            res = err.messages
        return res

    def delete(self, id):
        data = Subcategory.objects(id=id).delete()
        return jsonify(data)


class ProductResource(Resource):
    def get(self, id=None, category_id=None, subcategory_id=None):
        if id:
            post = Product.objects(id=id).first()
            post.add_view()
            json_obj = schemas.ProductSchema().dumps(post)
        else:
            if category_id:
                _category = Category.objects(id=category_id).first()
                _sabcategories = Subcategory.objects.filter(category=_category).all()
                data = Product.objects.filter(subcategory__in=_sabcategories).all()
            elif subcategory_id:
                _subcategory = Subcategory.objects(id=subcategory_id).first()
                data = Product.objects.filter(subcategory=_subcategory).all()
            else:
                data = Product.objects.all()

            json_obj = schemas.ProductSchema(many=True).dumps(data)

        return jsonify(json.loads(json_obj))

    def post(self):
        json_data = request.get_json(force=True)
        try:
            res = self.edit(json_data)
            Product.objects.create(**res)
            res = json.loads(schemas.ProductSchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, id):
        json_data = request.get_json(force=True)
        try:
            res = self.edit(json_data)
            Product.objects(id=id).update(**res)
            data = Product.objects(id=id).first()
            json_obj = schemas.ProductSchema().dumps(data)
            res = jsonify(json.loads(json_obj))
        except ValidationError as err:
            res = err.messages
        return res

    def delete(self, id):
        data = Product.objects(id=id).delete()
        return jsonify(data)

    def edit(self, json_data):
        res = schemas.ProductSchema().loads(json.dumps(json_data))
        res['subcategory'] = Subcategory.objects.filter(name=json_data['subcategory']['title']).first()
        return res


class TotalResource(Resource):
    def get(self):
        data = Product.objects.all()
        agr = 0
        if len(data):
            for row in data:
                agr += row.price

            agr = round(agr / len(data), 2)

        # json_obj = schemas.ProductSchema(many=True).dumps(data)

        return jsonify(agr)
