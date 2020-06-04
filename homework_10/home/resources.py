from flask_restful import Resource
from homework_10.home.models import *
from flask import request, jsonify
import json


class CategoryResource(Resource):
    def get(self, id=None):
        if id:
            data = Category.objects(id=id).first().to_json()
        else:
            data = Category.objects.all().to_json()
        return jsonify(json.loads(data))

    def post(self):
        _post = request.get_json(force=True)
        data = Category.objects.create(**_post)
        return jsonify(json.loads(data.to_json()))

    def put(self, id):
        _post = request.get_json(force=True)
        data = Category.objects(id=id).update(**_post)
        return jsonify(data)

    def delete(self, id):
        data = Category.objects(id=id).delete()
        return jsonify(data)


class SubcategoryResource(Resource):
    def get(self, id=None):
        if id:
            data = Subcategory.objects(id=id).first().to_json()
        else:
            data = Subcategory.objects.all().to_json()
        return jsonify(json.loads(data))

    def post(self):
        _post = request.get_json(force=True)
        data = Subcategory.objects.create(**_post)
        return jsonify(json.loads(data.to_json()))

    def put(self, id):
        _post = request.get_json(force=True)
        data = Subcategory.objects(id=id).update(**_post)
        return jsonify(data)

    def delete(self, id):
        data = Subcategory.objects(id=id).delete()
        return jsonify(data)


class ProductResource(Resource):
    def get(self, id=None, category_id=None, subcategory_id=None):
        if id:
            post = Product.objects(id=id).first()
            post.add_view()
            data = post.to_json()
        elif subcategory_id:
            _subcategory = Subcategory.objects(id=subcategory_id).first()
            data = Product.objects.filter(subcategory=_subcategory).to_json()
        elif category_id:
            _category = Subcategory.objects(id=category_id).first()
            data = Subcategory.objects.filter(category=_category).to_json()
        else:
            data = Product.objects().all().to_json()
        return jsonify(json.loads(data))

    def post(self):
        _post = request.get_json(force=True)
        data = Product.objects.create(**_post)
        return jsonify(json.loads(data.to_json()))

    def put(self, id):
        _post = request.get_json(force=True)
        data = Product.objects(id=id).update(**_post)
        return jsonify(data)

    def delete(self, id):
        data = Product.objects(id=id).delete()
        return jsonify(data)

class TotalResource(Resource):
    pass

