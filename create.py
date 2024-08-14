import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
query = ("create table student(st_id INT primary key auto_increment, st_name varchar(50), st_class varchar(50), "
         "st_email varchar(50))")
curs.execute(query)
