import pymysql as mq

my = mq.connect(host="localhost", user="root", password="", database="python")
curs = my.cursor()
print("{:<15}{:<20}{:<20}{:<30}{:<10}".format("Id", "Name", "Class", "email", "Fee"))

try:
    query = ("select student_fee.id, student.st_name, student.st_class, student.st_email, student_fee.fee_amount "
             "from student_fee, student where student_fee.student_id = student.st_id")
    curs.execute(query)
    data = curs.fetchall()
    for n in data:
        # print(n[4])
        print("{:<15}{:<20}{:<20}{:<30}{:<10}".format(n[0], n[1], n[2], n[3], n[4]))
except:
    print("error")

