import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
print("{:<15}{:<20}{:<20}".format("Id","Student_id","Fee"))

try:
    query = "select * from student_fee where student_id between 1 and 2"
    curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("{:<15}{:<20}{:<20}".format(n[0],n[1],n[2]))
except:
    print("error")
