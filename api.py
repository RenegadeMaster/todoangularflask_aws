from flask import Blueprint, request
from flask.ext.restful import Api, Resource, fields, marshal_with
from werkzeug.datastructures import ImmutableDict
from models import Todo, db

api = Api(prefix='/api')
api_bp = Blueprint('api_bp', __name__)
api.init_app(api_bp)

todo_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'date': fields.DateTime,
    'done': fields.Boolean
}


class TodoListResource(Resource):
    @marshal_with(todo_fields)
    def get(self):
        return Todo.query.all()

    @marshal_with(todo_fields)
    def post(self):
        new = Todo(request.json['task'], False)
        db.session.add(new)
        db.session.commit()
        return new, 201

    def put(self):
        tasks = Todo.query.all()
        for task in tasks:
            task.done = True
        db.session.commit()
        return '', 204

    def delete(self):
        if request.args.get('done'):
            to_delete = Todo.query.filter_by(done=True)
        else:
            to_delete = Todo.query.all()
        for item in to_delete:
            db.session.delete(item)
        db.session.commit()
        return '', 204


class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self, todo_id):
        res = Todo.query.get(todo_id)
        if res:
            return res
        return {'error': 'The specified id was not found in the DB'}, 400

    def delete(self, todo_id):
        to_delete = Todo.query.get(todo_id)
        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return '', 204
        return {'error': 'The specified id was not found in the DB'}, 400

    def put(self, todo_id):
        to_modify = Todo.query.get(todo_id)
        if to_modify and request.json:
            to_modify.task = request.json.get('task', to_modify.task)
            to_modify.done = request.json.get('done', to_modify.done)
            db.session.commit()
            return '', 204
        return {}, 400

api.add_resource(TodoListResource, '/todo')
api.add_resource(TodoResource, '/todo/<string:todo_id>')