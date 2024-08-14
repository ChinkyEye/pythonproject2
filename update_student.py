import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
student_id = input("Enter the student ID:")
student_name = input("Enter the desired Name:")
try:
    query = "update student set st_name ='"+student_name+"' where st_id =" +student_id
    # query = "update student set st_name = %s where st_id = %s"
    # data = (student_name, student_id)
    # curs.execute(query, data)
    curs.execute(query)
    my.commit()
    print("Data Updated")
except:
    print("error")