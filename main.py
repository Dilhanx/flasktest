from flask import Flask, request, render_template
from logging.handlers import RotatingFileHandler
import json
import requests
import pyodbc 
import logging
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
  app.logger.info("Test")
  return 'Hello, World!'
@app.route('/q')
def hello_world():
  return 'qq'
@app.route('/test',methods=['POST'])
def test():
  account=[]
 
  data=("username : "+request.form['username'],"password : "+request.form['password'])
  print (data)
  account.append(data)
  j = json.dumps(data)
  print (j)
  return j






@app.route('/ain')
def ain():
  return render_template('main.html')

@app.route('/search')

@app.route('/streamer/<streamername>')
def streamer(streamername):
  return streamername

@app.route('/streamer/<streamername>/comment')
def streamercomment(streamername):
  return ""+streamername+"comment"

@app.route('/login',methods=['POST'])
def login():
    print("Start")
    file = open("D:/New folder (26)/dbc.txt", "r")
    text = file.readline().split(",")
    print("File open")
    # Asign values to  send

    # Asign database connection details
    server = "kappaorbannedj.database.windows.net"

    database = "TwitchStats"

    username = "Dilhan@kappaorbannedj"

    password = "101Luminous101"
   
    driver="{ODBC Driver 13 for SQL Server}" 
    file.close()
    print("File close")

    #Driver={ODBC Driver 13 for SQL Server};Server=tcp:kappaorbanned.database.windows.net,1433;Database=TwitchStats;Uid=Dilhan@kappaorbanned;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
    #db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    print("DB Set")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print (request.form['username'] +" "+request.form['password'])
    cursor.execute("SELECT count(*) As cou From user_account where username= '"+request.form['username']+"' AND password ='"+request.form['password']+"' ;")
    row = cursor.fetchone()
    print(row)
    if row.cou==1:
      return "{\"status\": \"login\"}"
    else:
      return "{\"status\": \"incorrect\"}"



@app.route('/foo')
def foo():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return "foo"
if __name__ == '__main__':
  formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") #Set log message formate
  handler = RotatingFileHandler("log/"+time.strftime("%Y-%m-%d ")+".log", maxBytes=10000, backupCount=1) 
  handler.setLevel(logging.INFO) 
  handler.setFormatter(formatter)
  app.logger.addHandler(handler) 
  app.logger.setLevel(logging.INFO)
  
  app.run()
