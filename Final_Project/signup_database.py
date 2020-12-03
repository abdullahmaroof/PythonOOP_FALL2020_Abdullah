from sqlite3 import *

con = connect("userdata.db")
#sql = """CREATE TABLE user_data (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email_id TEXT, age INTEGER, password TEXT)"""
cursor = con.cursor()
#cursor.execute(sql)

con.commit()
con.close()
