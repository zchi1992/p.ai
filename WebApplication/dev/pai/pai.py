import os
import sqlite3
from flask import Flask, g, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__, instance_relative_config=True)
# app.config.from_pyfile('app.cfg', silent = True)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////pai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
######################################################################################
# Database Connection
######################################################################################
db = SQLAlchemy(app)
# db connect
# def connect_db():
#     """connect to database"""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv

# # initialize a database
# def init_db():
#     db = get_db()
#     with app.open_resource('schema.sql', mode = 'r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()

# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     init_db()
#     print('Initialized the databse.')

# # helper function to get db connection
# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db

# # disconnect with database
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

######################################################################################
# User class
######################################################################################
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(30))


######################################################################################
# User Login
######################################################################################
@app.route('/')
def index():
    return render_template('index.html')

# ######################################################################################
# # User Login
# ######################################################################################
login_manager = LoginManager()
login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@app.route('/<username>')
def log_in(username):
    user = User.query.filter_by(username=username).first()
    login_user(user)
    return 'You are now logged in'

@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return 'You are now logged out'

@app.route('/home')
@login_required
def home():
    return 'The current user is ' +  current_user.username

    
# @app.route('/disease', method=['GET'])
# def list_disease()

# @app.route('/search', method=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
    

