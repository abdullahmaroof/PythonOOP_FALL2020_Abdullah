from cx_Oracle import *

con = connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")
cursor = con.cursor()
name = str(input("Name: "))
password = str(input("Password: "))
#sql = """CREATE TABLE UserData (firstname VARCHAR2(50), secondname VARCHAR2(50), email VARCHAR2(50), age NUMBER(3), password VARCHAR2(50))"""
#sql = """INSERT INTO UserData VALUES ('zubair','ali','zubair@gmail.com',20,'1234')"""
#sql = "SELECT * FROM UserData WHERE firstname = %s AND password = %s",(str(name),str(password))
cursor.execute(sql)
con.commit()
con.close()
