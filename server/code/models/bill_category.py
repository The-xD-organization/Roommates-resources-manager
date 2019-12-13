from db import db


class BillCategoryModel(db.Model):

    __tablename__ = 'bill_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    bill = db.relationship('BillModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self, extended=True):
        if extended:
            return {'id': self.id,
                    'name': self.name,
                    'bills': [bill.json() for bill in self.bill.all()]}
        return {'id': self.id,
                'name': self.name}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()