from sqlite3 import *

con = connect("UserData.db")
#sql = """CREATE TABLE User_Data (first_name TEXT, last_name TEXT, email_id TEXT, age INTEGER, password TEXT)"""

cursor = con.cursor()
#cursor.execute(sql)

con.commit()
con.close()
