from flask import Flask
from routing import views
from models import db


app = Flask(__name__)

# Configuring Database

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brokenai.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.2.12/brokenai'

# Initializing Database
db.init_app(app)

app.app_context().push()

# Blueprint for routing
app.register_blueprint(views, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
