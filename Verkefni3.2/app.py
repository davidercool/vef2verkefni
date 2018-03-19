from flask import *
from sqlalchemy import *
from sqlite3 import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
try: from Verkefni32 import config
except: from config import Config
db = SQLAlchemy(Config)
app = Flask(__name__)
app.config.from_object(Config)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)

class searchdb(FlaskForm):
    results = StringField('results', validators=[DataRequired("You need to insert a product name")])
    search = SubmitField('Search')

@app.route('/', methods=["POST",'GET'])
def forms():
    form = searchdb()
    if form.validate_on_submit():
        return render_template('results.html')
    else:
        return render_template('index.html', form=form)
app.run("0.0.0.0", port=8080)
