import pyodbc 
import requests
server = "kappaorbannedj.database.windows.net"

database = "TwitchStats"

username = "Dilhan@kappaorbannedj"

password = "101Luminous101"

driver="{ODBC Driver 13 for SQL Server}" 

#Driver={ODBC Driver 13 for SQL Server};Server=tcp:kappaorbanned.database.windows.net,1433;Database=TwitchStats;Uid=Dilhan@kappaorbanned;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
#db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
print("done")
cursor = db.cursor()
cursor.execute("SELECT count(*) From user_account;")
row = cursor.fetchone()
print (row)