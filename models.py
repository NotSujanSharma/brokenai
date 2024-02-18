from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db=SQLAlchemy()

# Create Model

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_details = db.relationship("User_details", backref="user", uselist=False)

    def __repr__(self):
        return f"User('{self.username}')"

class User_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey('users.username'), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=True)
    company = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
