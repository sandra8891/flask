from flask import Flask,render_template,request,redirect
# import sqlite3
App=Flask(__name__)
import mysql.connector

# con=sqlite3.connect("database.db")
# con.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,age int)")

con = mysql.connector.connect(
    host="localhost",
    user="sandra",
    password="sandra",
    database="sandra"
)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user(name TEXT,age int)")

@App.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        print(name,age)
        cur = con.cursor()
        cur.execute("INSERT INTO user(name,age) VALUES(%s,%s)",(name,age))
        # con=sqlite3.connect("database.db")
        # con.execute("insert into users(name,age) values(?,?)",(name,age))
        con.commit()
        con.close()
        return redirect("/")
    return render_template("index.html")

App.run()