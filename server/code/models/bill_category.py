from db import db


class BillCategoryModel(db.Model):

    __tablename__ = 'bill_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    bill = db.relationship('BillModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name,
                'bills': [bill.json() for bill in self.bill.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()