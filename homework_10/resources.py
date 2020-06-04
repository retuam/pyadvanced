from flask_restful import Resource
from homework_10.models import Author, Tag, Post
from flask import request, jsonify
import json


class AuthorResource(Resource):
    def get(self, id=None):
        if id:
            _author = Author.objects(id=id).first()
            data = Post.objects.filter(author=_author).to_json()
        else:
            data = Author.objects.all().to_json()
        return jsonify(json.loads(data))

    def post(self):
        _post = request.get_json(force=True)
        data = Author.objects.create(**_post)
        return jsonify(json.loads(data.to_json()))

    def put(self, id):
        _post = request.get_json(force=True)
        data = Author.objects(id=id).update(**_post)
        return jsonify(data)

    def delete(self, id):
        data = Author.objects(id=id).delete()
        return jsonify(data)


class TagResource(Resource):
    def get(self, id=None):
        if id:
            data = Tag.objects(id=id).first().to_json()
        else:
            data = Tag.objects.all().to_json()
        return jsonify(json.loads(data))

    def post(self):
        _post = request.get_json(force=True)
        data = Tag.objects.create(**_post)
        return jsonify(json.loads(data.to_json()))

    def put(self, id):
        _post = request.get_json(force=True)
        data = Tag.objects(id=id).update(**_post)
        return jsonify(data)

    def delete(self, id):
        data = Tag.objects(id=id).delete()
        return jsonify(data)


class PostResource(Resource):
    def get(self, id=None):
        if id:
            post = Post.objects(id=id).first()
            post.add_view()
            data = post.to_json()
        else:
            data = Post.objects().all().to_json()
        return jsonify(json.loads(data))

    def post(self):
        _post = request.get_json(force=True)
        data = Post.objects.create(**_post)
        return jsonify(json.loads(data.to_json()))

    def put(self, id):
        _post = request.get_json(force=True)
        data = Post.objects(id=id).update(**_post)
        return jsonify(data)

    def delete(self, id):
        data = Post.objects(id=id).delete()
        return jsonify(data)
