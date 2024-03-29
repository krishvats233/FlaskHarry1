from datetime import datetime
import mysql.connector

from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
app.app_context().push()
#mysql://root:Trilokeshwar@29@localhost/alchemy

#sqlite:///todo.db


class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=True)
    email = db.Column(db.String(80),nullable=True)
    date_create = db.Column(db.DateTime,default=datetime.now())
    def __repr__(self) -> str:
          return f"{self.username}-> {self.email} -> on date {self.date_create}"
    def __init__(self,username,email):

           self.username=username
           self.email=email




@app.route('/add', methods=['POST'])
def hello_world():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Trilokeshwar@29",
        database="blog_app"
    )

    if conn.is_connected():
        print("Connected to MySQL database")

        # Perform database operations
        cursor = conn.cursor()

        # Example: Execute a query
        cursor.execute("SELECT * FROM user ")
        rows = cursor.fetchall()

        # Example: Print fetched rows
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        conn.close()
        print("MySQL connection closed")
    else:
        print("Failed to connect to MySQL database")

    # primary key ki value ye khud set kr letaa hai
    username = request.form['username']
    email = request.form['email']
       
    todo = Todo(username,email)
       
    db.session.add(todo)
    #db.session.add(admin)
    db.session.commit()

    return render_template('add.html')


#ham ab bascially ek class bangye for database taki flask ko bata ske ki hame kasia atble chaiya





#jijja 2 ek templating engine hai ye help krega ab ham html file mai apna python ke vatibale function.object ye sab use kr skte hai






@app.route('/todo')
def index():
    todo = Todo.query.all()
    return render_template('index1.html', users=todo)


@app.route('/')
def indexReturn():
    return render_template('index.html')



#delete a particular todo
@app.route('/delete/<int:sno>')
def delete(sno):
    allTodo=Todo.query.filter_by(id=sno).first()#means hame vo vali query dedo jiska sno eqyal ho jo hamne bheja
    db.session.delete(allTodo)
    db.session.commit()
    # return redirect("/")

    return render_template('delete.html')

#update a record
@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if(request.method=='POST'):
        # primary key ki value ye khud set kr letaa hai
        username = request.form['username']
        email = request.form['email']
        allTodo = Todo.query.filter_by(id=sno).first()
        allTodo.email=email
        allTodo.username=username
        db.session.add(allTodo)
        db.session.commit()
        return redirect("/")


    allTodo=Todo.query.filter_by(id=sno).first()#means hame vo vali query dedo jiska sno eqyal ho jo hamne bheja

    # return redirect("/")

    return render_template('update.html',todo=allTodo)

#





if(__name__=="__main__"):
  app.run( debug=True, port=8200)  # debug=true means agar koi problem aaye tho vo hame bowser mai hea dikh jayee
