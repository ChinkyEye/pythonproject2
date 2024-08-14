import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
print("{:<15}".format("Fee"))

try:
    query = "select max(fee_amount) from student_fee"
    curs.execute(query)
    data = curs.fetchall()
    for n in data:
        # print(n)
        print("{:<15}".format(n[0]))
except:
    print("error")
