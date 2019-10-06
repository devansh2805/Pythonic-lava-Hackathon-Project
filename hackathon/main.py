from flask import Flask,render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length
import os, sqlite3, csv
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import pandas as pd


app = Flask(__name__)

app.config['SECRET_KEY']='7f371cc08c51329ecccf896cdf66d590'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_BINDS']={'file':'sqlite:///file.db'}
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

class filecontent(db.Model):
    __bind_key__='file'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(300))
    data=db.Column(db.LargeBinary)


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

@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method=="GET":
        return render_template('upload.html')
    elif request.method=="POST":
        file=request.files['inputFile']
        file.save(secure_filename(file.filename))

    with open("dron.csv","w") as copyfile:
            filewriter = csv.writer(copyfile)
            with open(file.filename,"r") as originalfile:
                filereader=csv.reader(originalfile)
                for row in filereader:
                    filewriter.writerow(row)

    return render_template('attendance.html')

@app.route("/upload1",methods=["GET","POST"])
def upload1():
    return render_template('attendance.html')


@app.route('/view',methods=["POST"])
def view():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS ex")
    df = pd.read_csv("dron.csv")
    df.to_sql('ex',conn,index=False)
    cur.execute("SELECT * FROM ex")
    row_data = cur.fetchall()

    return render_template('attendance_page.html', title='attendance page',data_in_sheets=row_data)

@app.route('/sbr',methods=['GET','POST'])
def sbr():
    return render_template('srb.html')

@app.route("/finalsub",methods=['GET','POST'])
def finalsub():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS ex")
    df = pd.read_csv("dron.csv")
    df.to_sql('ex',conn,index=False)
    cur.execute("SELECT * FROM ex")
    row_data = cur.fetchall()
    
    if (request.method == "POST"):
        field1 =int(request.form.get("field1", False))
        return render_template('searchrno.html' , rno = field1 ,data_in_sheets=row_data)

@app.route('/bs',methods=['GET','POST'])
def bs():
    return render_template('slb.html')

@app.route("/lfinalsub",methods=['GET','POST'])
def lfinalsub():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS ex")
    df = pd.read_csv("dron.csv")
    df.to_sql('ex',conn,index=False)
    cur.execute("SELECT * FROM ex")
    row_data = cur.fetchall()
    
    if (request.method == "POST"):
        field2 =int(request.form.get("field2", False))
        return render_template('searchlect.html' , rno = field2 ,data_in_sheets=row_data)



@app.route('/allpre',methods=["POST"])
def allpre():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS ex")
    df = pd.read_csv("dron.csv")
    df.to_sql('ex',conn,index=False)
    cur.execute("SELECT * FROM ex")
    row_data = cur.fetchall()

    return render_template('ap.html', title='attendance page',data_in_sheets=row_data)

@app.route('/allab',methods=["POST"])
def allab():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS ex")
    df = pd.read_csv("dron.csv")
    df.to_sql('ex',conn,index=False)
    cur.execute("SELECT * FROM ex")
    row_data = cur.fetchall()

    return render_template('aa.html', title='attendance page',data_in_sheets=row_data)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

