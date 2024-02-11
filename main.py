from flask import Flask, render_template, request, redirect, url_for
from authorization import authorized, generate_jwt
from flask import make_response

app = Flask(__name__)

@app.route('/profile', methods=['GET'])  # Corrected line
def profile():
    # Store the authorization token from header in a variable
    token = request.cookies.get('Authorization')    
    if token:
        if authorized(token) == True:
            return render_template('profile.html')

    # Provide new authorization token in header
    #temp_token = generate_jwt('nau')
    response = make_response(redirect(url_for('login')))
    #response.set_cookie('Authorization', temp_token)
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'sujan' and password == 'password':
            token = generate_jwt(username)
            response = make_response(redirect(url_for('profile')))
            response.set_cookie('Authorization', token)
            return response
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect(url_for('home')))
    response.set_cookie('Authorization', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
