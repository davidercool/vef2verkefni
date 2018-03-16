from flask import *
from sqlalchemy import *
from sqlite3 import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

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