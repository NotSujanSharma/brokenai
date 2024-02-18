from models import db, Users, User_details
from authorization import authorized

def add_user(username, password,email):
    user= Users(username=username, password=password, email=email)
    user_details=User_details(username=username, email=email)
    user.user_details = user_details
    db.session.add(user)
    db.session.add(user_details)
    
    db.session.commit()
    return True

def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return user

def get_user_details(username):
    user_details = User_details.query.filter_by(username=username).first()
    return user_details

def get_all_users():
    users = Users.query.all()
    return users

def delete_user(username):
    user = Users.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return True

def update_user(username, password):
    user = Users.query.filter_by(username=username).first()
    user.password = password
    db.session.commit()
    return True

def validate_user(username, password):
    user = Users.query.filter_by(username=username).first()
    if user.password == password:
        return True
    return False

def logged_in(token):
    if(token):
        if (authorized(token) == True):
            return True
    return False