from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)


app.config['SECRET_KEY'] = '4be7e7dbe3e5f7807889d0090ac6a692'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


from blog import routes