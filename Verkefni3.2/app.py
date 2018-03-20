from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
try: from Verkefni32 import config
except: from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
class person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer)
    def __repr__(self):
        return '<User {}>'.format(self.name)

class searchdb(FlaskForm):
    results = StringField('results', validators=[DataRequired("Please enter a name")])
    search = SubmitField('Search')

'''
db.create_all()
db.session.add(person(name="Bob", age=40))
db.session.add(person(name="John", age=240))
db.session.add(person(name="David", age=18))
db.session.add(person(name="Benedict", age=38))
db.session.add(person(name="Cumberbatch", age=38))
db.session.commit()
'''

@app.route('/', methods=["POST",'GET'])
def forms():
    form = searchdb()
    listi=person.query.all()
    if form.validate_on_submit():
        return render_template('results.html', len=len, listi=listi, )
    else:
        print(form.productName.data.lower())
        return render_template('index.html', form=form)
app.run("0.0.0.0", port=8080)
