import flask
from flask import Flask,Response, flash, jsonify, redirect, render_template, request, session
import pymongo
import os 


#app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config["TEMPLATES_AUTO_RELOAD"] = True

class Mongo:
 @staticmethod
 def connection():
  client = pymongo.MongoClient("mongodb+srv://asunder:Mongo456@cluster0.qro4afw.mongodb.net/?retryWrites=true&w=majority")
  return client
