from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f"User('{self.username}')"

class User_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.age}')"
