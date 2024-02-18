from flask import Blueprint, request, render_template, redirect, url_for, make_response
from authorization import generate_jwt, get_username
from utils import validate_user, add_user, get_all_users, logged_in,get_user_details
import datetime
views = Blueprint('views',__name__)


#profile page

@views.route('/profile', methods=['GET']) 
def profile():
    token = request.cookies.get('Authorization')    
    if (logged_in(token)):
        username = get_username(token)
        user=get_user_details(username)
        return render_template('profile.html', logged_in=True, user=user)

    response = make_response(redirect(url_for('views.login')))
    return response

#main page

@views.route('/')
def home():
    token = request.cookies.get('Authorization')
    return render_template('index.html', logged_in=logged_in(token))


#login page

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validate_user(username,password) == True:
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
        email= request.form['email']
        if(add_user(username, password,email)):
            return redirect(url_for('views.login'))
        
    return render_template('signup.html')


# Users page

@views.route('/users', methods=['GET'])
def users():
    token = request.cookies.get('Authorization')
    users = get_all_users()
    return render_template('users.html', users=users, logged_in=logged_in(token))

#logout

@views.route('/logout', methods=['GET','POST'])
def logout():
    response = make_response(redirect(url_for('views.home')))
    response.set_cookie('Authorization', '', expires=datetime.datetime.utcnow()+datetime.timedelta(days=5))
    return response

@views.route('/user/<username>', methods=['GET'])
def user(username):
    return f"Hello {username}"