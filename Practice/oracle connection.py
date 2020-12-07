from cx_Oracle import *



con = connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")

cursor = con.cursor()
#sql = """CREATE TABLE studentinfo (std_id NUMBER(10), std_name VARCHAR2(50), std_age NUMBER(3))"""
#sql = """INSERT INTO studentinfo VALUES (3,'Shifa',20)"""
sql = """SELECT * FROM studentinfo"""
cursor.execute(sql)
for data in cursor:
    print(data)
#con.commit()
cursor.close()
con.close()

