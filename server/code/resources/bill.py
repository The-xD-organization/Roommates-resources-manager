from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.bill import BillModel, datetime


class Bill(Resource):
    """The idea is to pass category_id / bill category in endpoint /bill/<str:category_id>
        and the rest of data in json"""
    parser = reqparse.RequestParser()
    parser.add_argument('usage',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required()
    def get(self, category_id):
        """returns latest bill of given category"""
        try:
            bill = BillModel.find_latest_bill(category_id)
        except:
            return {"message": "An error occurred finding the item."}, 500  # Internal server error

        if bill:
            return bill.json()
        return {'message': 'Bill not found'}, 404

    @jwt_required
    def post(self, category_id):
        """create one bill of given category for a day"""
        last_bill = BillModel.find_latest_bill(category_id)
        if last_bill.date == datetime.today():
            return {'message': "Bill of given category with today's date already exists"}, 400

        data = Bill.parser.parse_args()

        bill = BillModel(data['usage'], data['description'], category_id)
        try:
            bill.save_to_db()
        except:
            return {'message': "An error occurred inserting the bill."}, 500

        return bill.json(), 201

    @jwt_required
    def delete(self):
        pass


class BillList(Resource):
    @jwt_required
    def get(self):
        """return json of every bill"""
        return {'bills': [bill.json() for bill in BillModel.query.all()]}
