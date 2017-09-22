import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from gevent.wsgi import WSGIServer

print('app configuration ran')
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('..\\instance\\app.cfg', silent = True)

# db connect
def connect_db():
    """connect to database"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factor = sqlite3.Row
    return rv

# initialize a database
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the databse.')

# helper function to get db connection
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# disconnect with database
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('')


http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
    

