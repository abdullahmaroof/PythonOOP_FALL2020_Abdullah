from cx_Oracle import *

con = connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")
cursor = con.cursor()
#sql = """CREATE TABLE bill (billno NUMBER(4), food VARCHAR2(20), flavour VARCHAR2(20), size VARCHAR2(20), price NUMBER(8))"""
#sql = """INSERT INTO BillData VALUES (1786,'pizza','smoke mexico','medium 8\"',800)"""
#cursor.execute(sql)
con.commit()
con.close()