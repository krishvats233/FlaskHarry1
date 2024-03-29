from flask import Flask,render_template
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_ROOT']='root'
app.config['MYSQL_PASSWORD']='Trilokeshwar@29'
app.config['MYSQL_DB']=('blog_app')
mysql=MySQL(app)




@app.route("/")
def hello():
    curr=mysql.connection.cursor()
    curr.execute("select * from user")
    fetchdata=curr.fetchall()
    curr.close()
    return render_template("index.html",data=fetchdata)

if(__name__=="__main__"):
  app.run( debug=True, port=8000)  # debug=true means agar koi problem aaye tho vo hame bowser mai hea dikh jayee
