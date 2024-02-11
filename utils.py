from models import db, Users

def add_user(username, password):
    user= Users(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return True

def get_all_users():
    users = Users.query.all()
    return users