from flask_restful import Resource
from homework_10.practice.models import Author, Tag, Post
from flask import request, jsonify
import json
from homework_10.practice import schemas
from marshmallow import ValidationError


class AuthorResource(Resource):
    def get(self, id=None):
        if id:
            _author = Author.objects(id=id).first()
            data = Post.objects.filter(author=_author).all()
            json_obj = schemas.PostSchema(many=True).dumps(data)
        else:
            data = Author.objects.all()
            json_obj = schemas.AuthorSchema(many=True).dumps(data)
        return jsonify(json.loads(json_obj))

    def post(self):
        json_data = json.dumps(request.json)
        try:
            res = schemas.AuthorSchema().loads(json_data)
            Author.objects.create(**res)
            res = json.loads(schemas.AuthorSchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, id):
        json_data = json.dumps(request.json)
        try:
            res = schemas.AuthorSchema().loads(json_data)
            data = Author.objects(id=id).update(**res)
            res = jsonify(data)
        except ValidationError as err:
            res = err.messages
        return res

    def delete(self, id):
        data = Author.objects(id=id).delete()
        return jsonify(data)


class TagResource(Resource):
    def get(self, id=None):
        if id:
            data = Tag.objects(id=id).first()
            json_obj = schemas.TagSchema().dumps(data)
        else:
            data = Tag.objects.all()
            json_obj = schemas.TagSchema(many=True).dumps(data)
        return jsonify(json.loads(json_obj))

    def post(self):
        json_data = json.dumps(request.json)
        try:
            res = schemas.TagSchema().loads(json_data)
            Tag.objects.create(**res)
            res = json.loads(schemas.TagSchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, id):
        json_data = json.dumps(request.json)
        try:
            res = schemas.TagSchema().loads(json_data)
            Tag.objects(id=id).update(**res)
            data = Tag.objects(id=id).first()
            json_obj = schemas.TagSchema().dumps(data)
            res = jsonify(json.loads(json_obj))
        except ValidationError as err:
            res = err.messages
        return res

    def delete(self, id):
        data = Tag.objects(id=id).delete()
        return jsonify(data)


class PostResource(Resource):
    def get(self, id=None):
        if id:
            post = Post.objects(id=id).first()
            post.add_view()
            json_obj = schemas.PostSchema().dumps(post)
        else:
            data = Post.objects().all()
            json_obj = schemas.PostSchema(many=True).dumps(data)
        return jsonify(json.loads(json_obj))

    def post(self):
        json_data = request.get_json(force=True)
        try:
            res = self.edit(json_data)
            Post.objects.create(**res)
            res = json.loads(schemas.PostSchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, id):
        json_data = request.get_json(force=True)
        try:
            res = self.edit(json_data)
            Post.objects(id=id).update(**res)
            data = Post.objects(id=id).first()
            json_obj = schemas.PostSchema().dumps(data)
            res = jsonify(json.loads(json_obj))
        except ValidationError as err:
            res = err.messages
        return res

    def delete(self, id):
        data = Post.objects(id=id).delete()
        return jsonify(data)

    def edit(self, json_data):
        res = schemas.PostSchema().loads(json.dumps(json_data))

        if json_data['author']['name'] and json_data['author']['surname']:
            author = Author.objects.filter(name=json_data['author']['name'],
                                           surname=json_data['author']['surname']).first()
            if not author:
                Author.objects.create(name=json_data['author']['name'], surname=json_data['author']['surname'])
                author = Author.objects.filter(name=json_data['author']['name'],
                                               surname=json_data['author']['surname']).first()
        res['author'] = author

        tags = []
        for _tag in filter(lambda a: a['title'], json_data['tags']):
            tag = Tag.objects.filter(title=_tag['title']).first()
            if not tag:
                Tag.objects.create(title=_tag['title'])
                tag = Tag.objects.filter(title=_tag['title']).first()
            tags.append(tag)

        res['tags'] = tags

        return res
