from flask_jwt import jwt_required, current_identity
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
    parser = reqparse.RequestParser()   #for put request
    parser.add_argument('bank_account',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @classmethod        # todo add admin privilage
    @jwt_required()
    def get(cls):
        user = UserModel.find_by_id(current_identity.id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod         # todo add admin privilage
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200

    @jwt_required()
    def put(self):
        """Method to update user's bank account field"""
        data = User.parser.parse_args()

        user = UserModel.find_by_id(current_identity.id)
        if user is None:
            return {'message': "There is no user with this ID, or your access_token is invalid."}
        else:
            user.bank_account = data['bank_account']

        user.save_to_db()

        return user.json()
