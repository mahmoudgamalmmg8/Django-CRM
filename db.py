import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Nope Not This Time'

)
#prepare a cursor object

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE crmdb")
print("ALLL DONE!")
