from cx_Oracle import *

con = connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")
cursor = con.cursor()
#sql = """CREATE TABLE MenuData (fastfood VARCHAR2(20), taste1 VARCHAR2(20), taste2 VARCHAR2(20), taste3 VARCHAR2(20), taste4 VARCHAR2(20), taste5 VARCHAR2(20))"""
#sql = """INSERT INTO MenuData VALUES ('Pizza','Chicken Fajita','Peeri Peeri','Smoke Mexico','Cheese Fajita','Thikka BarBQ')"""
#sql = """INSERT INTO MenuData VALUES ('Burger','Zinger','Beef','Chicken','Shotgun','BarBQ')"""
#sql = """INSERT INTO MenuData VALUES ('Biryani','Zinger','Beef','Chicken','Chinese Rice','BarBQ')"""
#sql = """INSERT INTO MenuData VALUES ('Paratha Roll','Zinger','Beef','Chicken','Smoke','BarBQ')"""
#sql = """SELECT * FROM MenuData"""
#cursor.execute(sql)
#for row in cursor:
 #   print(row)
con.commit()
con.close()