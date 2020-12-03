from sqlite3 import *

con = connect("mystudent.db")
#sql = """CREATE TABLE student (id INTEGER, name TEXT, marks INTEGER)"""
#sql = """INSERT INTO student VALUES (5,'Shifa',290)"""

cursor = con.cursor()
#cursor.execute(sql)

con.commit()
con.close()
