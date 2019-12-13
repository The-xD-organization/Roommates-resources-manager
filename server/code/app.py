import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister, User
from resources.bill import Bill, BillList
from resources.bill_category import BillCategory, BillCategoryList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # turns off flask_sqlalchemy modification tracker
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'bart'

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

# TODO usun przed wrzuceniem na heroku
# @app.before_first_request
# def create_tables():
#     db.create_all()


jwt = JWT(app, authenticate, identity)  # creates /auth endpoint

api.add_resource(BillCategory, '/bill_category/<string:name>')
api.add_resource(Bill, '/bill/<int:category_id>')
api.add_resource(BillList, '/bills')
api.add_resource(BillCategoryList, '/bill_categories')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

# if it's not __main__, it means we have imported this file (don't run the app then)
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)