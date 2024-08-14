import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
# print("{:<15}{:<20}".format("Count","Student_Id"))
print("{:<15}".format("Student_Id"))

try:
    # query = "select count(*), student_id from student_fee group by student_id"
    # query = "select distinct(student_id) from student_fee"
    # query = "select sum(fee_amount) from student_fee"
    # query = "select avg(fee_amount) from student_fee"
    query = "select count(*) from student_fee"
    curs.execute(query)
    data = curs.fetchall()
    for n in data:
        # print("{:<15}{:<20}".format(n[0],n[1]))
        print("{:<15}".format(n[0]))
except:
    print("error")
