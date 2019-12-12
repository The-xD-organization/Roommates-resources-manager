from flask_jwt_extended import jwt_required
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
    parser.add_argument('cash',
                        type=float,
                        required=False
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
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
        if BillModel.find_latest_bill(category_id):
            """if database is empty, this won't run"""
            last_bill = BillModel.find_latest_bill(category_id)

            if last_bill.date.day == datetime.today().day:
                return {'message': "Bill of given category with today's date already exists"}, 400

        data = Bill.parser.parse_args()

        bill = BillModel(data['usage'], data['cash'], data['description'], category_id)
        try:
            bill.save_to_db()
        except:
            return {'message': "An error occurred inserting the bill."}, 500

        return bill.json(), 201

    @jwt_required
    def delete(self, category_id):
        """delete latest bill of given category"""
        bill = BillModel.find_latest_bill(category_id)
        if bill:
            bill.delete_from_db()

        return {'message': 'Bill deleted'}


class BillList(Resource):
    @jwt_required
    def get(self):
        """return json of every bill"""
        return {'bills': [bill.json() for bill in BillModel.find_all()]}


