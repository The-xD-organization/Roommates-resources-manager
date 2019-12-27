from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse, inputs
from models.bill import BillModel
from models.user import UserModel


class Bill(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('category_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('usage',
                        type=float,
                        required=False,
                        help="This field cannot be left blank!")
    parser.add_argument('cash',
                        type=float,
                        required=False
                        )
    parser.add_argument('payer_account',
                        type=str,
                        required=False)

    is_payed_parser = reqparse.RequestParser()
    is_payed_parser.add_argument('is_payed',
                                 type=inputs.boolean,
                                 required=True,
                                 help="This field cannot be left blank!")

    @jwt_required()
    def get(self, bill_id):
        """returns latest bill of given category"""
        try:
            bill = BillModel.find_by_id(bill_id)
        except:
            return {"message": "An error occurred finding the item."}, 500  # Internal server error

        if bill:
            return bill.json()
        return {'message': 'Bill not found'}, 404

    @jwt_required()
    def post(self):
        """create one bill of given category for a day"""
        # TODO uncomment in production, FOR TEST ONLY
        data = Bill.parser.parse_args()
        # if BillModel.find_latest_bill(data['category_id']):
        #     """if database is empty, this won't run"""
        #     last_bill = BillModel.find_latest_bill(category_id)
        #
        #     if last_bill.date.day == datetime.today().day:
        #         return {'message': "Bill of given category with today's date already exists"}, 400
        user = UserModel.find_by_id(current_identity.id)
        if data["payer_account"] not in {"", None}:
            bill = BillModel(data['usage'],
                             data['cash'],
                             data['description'],
                             data['category_id'],
                             data['payer_account'])
        else:
            bill = BillModel(data['usage'], data['cash'], data['description'], data['category_id'], user.bank_account)

        try:
            bill.save_to_db()
        except:
            return {'message': "An error occurred inserting the bill."}, 500

        return bill.json(), 201

    @jwt_required()
    def put(self, bill_id):
        """method for updating field 'is_payed' which is type boolean"""
        is_payed_data = Bill.is_payed_parser.parse_args()

        bill = BillModel.find_by_id(bill_id)
        if bill is None:
            return {'message': "Bill with id {} doesn't exist".format(bill_id)}
        else:
            bill.is_payed = is_payed_data['is_payed']

        bill.save_to_db()

        return bill.json()

    @jwt_required()
    def delete(self, bill_id):
        """deletes bill with provided id"""
        bill = BillModel.find_by_id(bill_id)
        if bill:
            bill.delete_from_db()

        return {'message': 'Bill deleted'}


class BillList(Resource):
    @jwt_required()
    def get(self):
        """return json of every bill"""
        return {'bills': [bill.json() for bill in BillModel.find_all()]}
