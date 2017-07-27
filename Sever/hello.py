from flask import Flask
import json
import time
import requests
import pyodbc
app = Flask(__name__)
@app.route("/hello")
def login():
    return "Hello world"



