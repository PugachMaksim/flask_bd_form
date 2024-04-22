from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(36), unique=False, nullable=False)
    user_surname = db.Column(db.String(36), unique=False, nullable=False)
    user_email = db.Column(db.String(36), unique=True, nullable=False)
    create_acc = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return f'Account({self.user_name}, {self.user_surname}, {self.user_email})'
