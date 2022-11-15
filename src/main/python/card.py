import flask
from flask import Flask,Response, flash, jsonify, redirect, render_template, request, session
import sqlite3
import os 
from sqlite3 import Error
import jsonpickle

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["TEMPLATES_AUTO_RELOAD"] = True


def create_connection(db_file):
 conn = sqlite3.connect(db_file)

 return conn


def create_table(conn,create_table_sql):
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)

@app.route("/card")
def events():
 database="/home/asunder/pythonsqlite.db"
 #print(database)
 sql_create_projects_table="""CREATE TABLE CARDS IF NOT EXISTS(Card_Name VARCHAR(255),Gateway_Name VARCHAR(255),Country VARCHAR(255));"""
 conn = create_connection(database)
 print("Connection is",conn)
 #if conn is not None:
 #create_table(conn,sql_create_projects_table)
 #else:
 #print("Error! cannot create the database connection.")
 cur=conn.cursor()
 #print("Cursor",cur)
 conn.execute("""insert into CARDS (Card_Name,Gateway_Name,Country) values("MasterCard", "G1", "USA");""")
 conn.execute("""insert into CARDS (Card_Name,Gateway_Name,Country) values("Visa", "G2", "UK");""")
 conn.execute("""insert into CARDS (Card_Name,Gateway_Name,Country) values("StandardCharted", "G3", "India");""")
 conn.execute("""insert into CARDS (Card_Name,Gateway_Name,Country) values("CardMax", "G4", "Venezuela");""") 
 conn.execute("""insert into CARDS (Card_Name,Gateway_Name,Country) values("Conquele", "G5", "Argentina");""")
 k=conn.execute("SELECT Card_Name FROM CARDS;")
 objs=k.fetchall()

 def events():
  #print("Obj",str(objs),"\nType",type(objs))
  for el in objs:
    yield ''.join(el)
    yield '\n'
 return Response(events(),content_type='application/json')


if __name__=='main':
  app.run(debug=True,port=8082)

