import pymysql as mq

my = mq.connect(host="localhost", user="root", password="",database="python")
curs = my.cursor()
try:
    query = "insert into student(st_name, st_class,st_email) values(%s,%s,%s)"
    t=("Milan","five","khimdingmilan99@gmail.com")
    t=[("Milan","five","khimdingmilan99@gmail.com"), ("Sitam","six","sitam@gmail.com")]
    # curs.execute(query,t)
    curs.executemany(query,t)
    my.commit()
    print("Data was inserted")
except:
    print("error")
