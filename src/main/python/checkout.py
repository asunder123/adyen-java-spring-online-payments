import flask
from flask import Flask,Response, flash, jsonify, redirect, render_template, request, session
import sqlite3
import os 
from sqlite3 import Error
import jsonpickle
import pymongo
from conn import Mongo 

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["TEMPLATES_AUTO_RELOAD"] = True


def create_connection():
 #conn = sqlite3.connect(db_file)
 conn = pymongo.MongoClient("mongodb+srv://asunder:Mongo456@cluster0.bafj3mg.mongodb.net/?retryWrites=true&w=majority")
 return conn


def create_table(conn,create_table_sql):
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)
i=0
@app.route("/checkout")
def checkout():
 """
 database="/home/asunder/pythonsqlitetwo.db"

 sql_create_projects_table=""""CREATE TABLE CHECKM(Card_Valid VARCHAR(30),Status VARCHAR(30),CardNo VARCHAR(255));""""
 conn = create_connection(database)
 print("Connection is",conn)
 cur=conn.cursor()
 k=conn.execute("SELECT Status,CardNo FROM CHECKM;")
 """
 #try:
 client=create_connection()
 db=client.payment
 #print("Created payment db",db)
 table=db["checkout"]
 print("Table",table)
 hits=0
 myList={}
 for i in range(30):
  myList=[{"Categories": ["Cosmetics"] ,"cartitems": int(40)+i },{"Categories": ["Upholsteries","Consumables"] ,"cartitems": int(35)+i },{"Categories": ["Appliances","Groceries"],"cartitems": int(36)+i }]
  i+=1
 print(client.list_database_names())
 print("About to insert data into table...")
 x=table.insert_many(myList)

 def events():
  for x in table.find():
    yield str(x)
 return Response(events(),content_type='application/json')


if __name__=='main':
  app.run(debug=True,port=8082)

