import flask
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import sqlite3
import os 


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["TEMPLATES_AUTO_RELOAD"] = True




@app.route("/check")
def checkout():
 k=["Cart", "Hockey","Ice"]
 return str(k)  

if __name__=='main':
    app.run(port=8081)

