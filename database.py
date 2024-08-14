import pymysql as mq

# Establish a connection
my = mq.connect(host="localhost", user="root", password="")
curs = my.cursor()
try:
    db = "create database python"
    curs.execute(db)
    print("database created")
except:
    print("error..")
