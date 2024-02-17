import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mahmoud12mmg8'

)
#prepare a cursor object

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE crmdb")
print("ALLL DONE!")