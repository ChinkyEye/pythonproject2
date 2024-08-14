import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
print("{:<15}{:<20}{:<20}{:<10}".format("Id","Name","Class","email" ))

try:
    query = "select * from student"
    curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("{:<15}{:<20}{:<20}{:<10}".format(n[0],n[1],n[2],n[3]))
except:
    print("error")
