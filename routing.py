from flask import Blueprint, request, render_template, redirect, url_for, make_response
from authorization import authorized, generate_jwt
from models import db, Users
views = Blueprint('views',__name__)


#profile page

@views.route('/profile', methods=['GET']) 
def profile():
    token = request.cookies.get('Authorization')    
    if token:
        if authorized(token) == True:
            return render_template('profile.html')

    response = make_response(redirect(url_for('views.login')))
    #temp_token = generate_jwt('nau')
    #response.set_cookie('Authorization', temp_token)
    return response

#main page

@views.route('/')
def home():
    return render_template('index.html')


#login page

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'sujan' and password == 'password':
            token = generate_jwt(username)
            response = make_response(redirect(url_for('views.profile')))
            response.set_cookie('Authorization', token)
            return response
    return render_template('login.html')


# Signup page

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        user= Users(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        
        return redirect(url_for('views.login'))
        
    return render_template('signup.html')


# Users page

@views.route('/users', methods=['GET'])
def users():
    users = Users.query.all()
    return render_template('users.html', users=users)

#logout

@views.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect(url_for('views.home')))
    response.set_cookie('Authorization', '', expires=0)
    return response
