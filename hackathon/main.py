from flask import Flask,render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='7f371cc08c51329ecccf896cdf66d590'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class userinfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(50),nullable=False)
    department = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f"User('{self.name}','{self.surname}','{self.username}','{self.department}')"

class loginform(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')


@app.route('/',methods=['GET','POST'])
def login():
    form=loginform(request.form)
    error=None
    if request.method=="POST" and form.validate_on_submit():
        user=userinfo.query.filter_by(username=form.username.data).first()
        #if username entered is in database its record will be stored in user
        if not(user) or user.password!=form.password.data:
            error = 'Login Unsuccessful.Please check username and password'
        elif(user.password==form.password.data):
            #return "Login successful. Welcome "+user.name+" "+user.surname
            return render_template('home.html',title="Home Page",name=user.name,surname=user.surname,department=user.department)
    return render_template('login.html',title="Login",error=error,form=form)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

