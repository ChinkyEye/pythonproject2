import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
student_id = input("Enter the student ID:")
try:
    query = "delete from student where st_id = %s"
    curs.execute(query, student_id)
    my.commit()
    print("Data Deleted")
except:
    print("error")