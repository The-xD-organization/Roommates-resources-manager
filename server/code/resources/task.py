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

    updating_parser = reqparse.RequestParser()
    updating_parser.add_argument('is_done',
                                 type=inputs.boolean,
                                 required=False)

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
        if data['description'] not in {"", None}:
            task = TaskModel(data['description'])
        else:
            return {"message": "A task must have a description."}

        try:
            task.save_to_db()
        except:
            return {'message': "An error occurred inserting the bill."}, 500
        return task.json(), 201

    @jwt_required()
    def put(self, task_id):
        """update fields:
            -is_done
            -assignee_id --- currently logged in user"""
        data = Task.updating_parser.parse_args()

        task = TaskModel.find_by_id(task_id)
        if task is None:
            return {'message': "Task with id {} doesn't exist".format(task_id)}

        if task.assignee_id is None:
            user = UserModel.find_by_id(current_identity.id)
            #   assigning currently logged user to task
            task.assignee_id = user.id
            task.assignee_name = user.username

        if data['is_done']:
            #   updating is_done field
            task.is_done = data['is_done']
        else:
            return {'message': "{} is already assigned to this task".format(task.assignee_name)}, 400

        try:
            task.save_to_db()
        except:
            return {'message': "An error occurred inserting the task."}, 500

        return task.json(), 201



class TaskList(Resource):
    @jwt_required()
    def get(self):
        """return json of every task"""
        return {'tasks': [task.json() for task in TaskModel.find_all()]}
