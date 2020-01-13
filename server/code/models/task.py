from db import db
from datetime import datetime


class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    is_done = db.Column(db.Boolean, default=False, nullable=True)
    date_of_creation = db.Column(db.DateTime(timezone=False), default=datetime.today)
    assignee_name = db.Column(db.String(80), default=None)

    assignee_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=None)
    assignee = db.relationship('UserModel')

    def __init__(self, description, assignee_id=None, is_done=False):
        self.description = description
        self.assignee_id = assignee_id
        self.is_done = is_done

    def json(self):
        date = str(self.date_of_creation)
        return {'id': self.id,
                'assignee_name': self.assignee_name,
                'description': self.description,
                'is_done': self.is_done,
                'date_of_creation': date[:10]
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_my_tasks(cls, user_id):
        return cls.query.filter_by(assignee_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
