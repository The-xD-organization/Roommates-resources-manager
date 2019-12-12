from flask_restful import Resource
from models.bill_category import BillCategoryModel
from flask_jwt import jwt_required

class BillCategory(Resource):
    @jwt_required()
    def get(self, name):
        bill_category = BillCategoryModel.find_by_name(name)
        if bill_category:
            return bill_category.json()
        return {'message': 'Bill category not found.'}, 404


class BillCategoryList(Resource):
    @jwt_required()
    def get(self):
        return {'bill categories': [bill_category.json() for bill_category in BillCategoryModel.query.all()]}