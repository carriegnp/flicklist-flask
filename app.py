from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='temples')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flicklist:123456@localhost:8889/flicklist'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy()

with app.app_context():
    db.init_app(app)