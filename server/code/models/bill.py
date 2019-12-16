from db import db
from datetime import datetime


class BillModel(db.Model):

    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    usage = db.Column(db.Float(precision=2), default=0)
    date = db.Column(db.DateTime(timezone=False), default=datetime.today)
    cash = db.Column(db.Float(precision=2), default=0)
    description = db.Column(db.String(100))
    is_payed = db.Column(db.Boolean, default=0)     # 0 means not payed
    payer_account = db.Column(db.String(28), default="")

    category_id = db.Column(db.Integer, db.ForeignKey('bill_categories.id'))
    category = db.relationship('BillCategoryModel')

    def __init__(self, usage, cash, description, category_id,  payer_account="", is_payed=0,):
        self.usage = usage
        self.cash = cash
        self.description = description
        self.category_id = category_id
        self.is_payed = is_payed
        self.payer_account = payer_account

    def json(self):
        #TODO zwroc id rachunku, co by mozna bylo usuwac dowolny
        date = str(self.date)
        return {'id': self.id,
                'category_id': self.category_id,
                'usage': self.usage,
                'cash': self.cash,
                'date': date[:10],
                'is_payed': self.is_payed,
                'payer_account': self.payer_account,
                'description': self.description
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_latest_bill(cls, category_id):
        """returns latest bill of given category (with the most recent date) """
        return cls.query.filter_by(category_id=category_id).order_by(cls.date.desc()).first()

    def save_to_db(self):
        """Inserts/update the item to the database"""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()