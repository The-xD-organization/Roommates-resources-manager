import _sqlite3

from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # parses through json and makes sure username and password are there
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def post(self):
        """registers new user if it doesn't exist already"""
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User with username '{}' already exists.".format(data['username'])}, 400 # Bad request

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created succesfully."}, 201    # 201 - Created


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200