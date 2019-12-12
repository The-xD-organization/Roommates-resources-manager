import _sqlite3

from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import UserModel


# parses through json and makes sure username and password are there
# _ before user_parser means it's private and you should not import it
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be left blank!")
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be left blank!")


class UserRegister(Resource):

    def post(self):
        """registers new user if it doesn't exist already"""
        data = _user_parser.parse_args()

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


class UserLogin(Resource):

    @classmethod
    def post(cls):
        # get data from parser
        data = _user_parser.parse_args()

        # find user in database
        user = UserModel.find_by_username(data['username'])

        # check password
        # authenticate() function used to do this
        if user and safe_str_cmp(user.password, data['password']):
            # identity() function used to do identity=
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return{
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {'message': 'Błędne dane logowania'}, 401
