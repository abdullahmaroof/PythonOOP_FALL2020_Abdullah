from cx_Oracle import *

con = connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")
cursor = con.cursor()
#sql = """CREATE TABLE UserData (firstname VARCHAR2(50), secondname VARCHAR2(50), email VARCHAR2(50), age NUMBER(3), password VARCHAR2(50))"""
#sql = """INSERT INTO UserData VALUES ('zubair','ali','zubair@gmail.com',20,'1234')"""

#cursor.execute(sql)
con.commit()
con.close()
