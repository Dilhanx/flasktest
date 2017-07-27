from flask import Flask
import json
import time
import requests
import pyodbc
app = Flask(__name__)
@app.route("/accounts")
def login():
    print("Start")
    file = open("D:/New folder (26)/dbc.txt", "r")
    text = file.readline().split(",")
    print("File open")
    # Asign values to  send

    # Asign database connection details
    server = text[0]

    database = text[1]

    username = text[2]

    password = text[3]
   
    driver=text[4]    
    file.close()
    print("File close")
    #Driver={ODBC Driver 13 for SQL Server};Server=tcp:kappaorbannedj.database.windows.net,1433;Database=TwitchStats;Uid=Dilhan@kappaorbannedj;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
    #Driver={ODBC Driver 13 for SQL Server};Server=tcp:kappaorbanned.database.windows.net,1433;Database=TwitchStats;Uid=Dilhan@kappaorbanned;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
    #db =  pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    db =  pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};PORT=1433;SERVER=kappaorbannedj.database.windows.net;PORT=1443;DATABASE=TwitchStats;UID=Dilhan@kappaorbannedj;PWD=101Luminous101')
    print("DB Set")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT * From User_Account ")
    row = cursor.fetchone()
    x=0
    sql_list =[]
    while row:
        print (row.username +" " +row.email+ " "+row.password)
        data=(row.username , row.email,row.password)
        x+=1
        sql_list.append(data)
        row = cursor.fetchone()
    print( sql_list)
    j = json.dumps( sql_list)
    return j



if __name__ == '__main__':
  app.run()