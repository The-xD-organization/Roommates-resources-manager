from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse, inputs
from models.task import TaskModel
from models.user import UserModel


class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required()
    def get(self, task_id):
        """returns task with given id"""
        try:
            task = TaskModel.find_by_id(task_id)
        except:
            return {"message": "An error occurred finding the task."}, 500

        if task:
            return task.json()
        return {'message': 'Task not found'}, 404

    @jwt_required()
    def post(self):
        """create task"""
        data = Task.parser.parse_args()
        if data['description'] != "":
            task = TaskModel(data['description'])
        else:
            return {"message": "A task must have a description."}

        try:
            print(task.json())
            task.save_to_db()
        except Exception as E:
            return {'message': "{}".format(E)}, 500
        return task.json(), 201


class TaskList(Resource):
    @jwt_required()
    def get(self):
        """return json of every task"""
        return {'tasks': [task.json() for task in TaskModel.find_all()]}
