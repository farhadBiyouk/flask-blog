from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)


app.config['SECRET_KEY'] = '4be7e7dbe3e5f7807889d0090ac6a692'

#  Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
db = SQLAlchemy(app)

#  For hashing password
bcrypt = Bcrypt(app)

#  Login config
login_manger = LoginManager(app)
login_manger.login_view = 'login'
login_manger.login_message = 'Please the first time logged in '
login_manger.login_message_category = 'info'


#  Mapping routes
from blog import routes