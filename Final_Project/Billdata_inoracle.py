import cx_Oracle
def bill(billno,food,flavour,size,price):
    conn = cx_Oracle.connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")
    cur = conn.cursor()
    oracle = "INSERT INTO BillData VALUES ('" + str(billno) + "','" + food + "','" + flavour + "','" + size + "','" + str(price) + "')"
    cur.execute(oracle)
    conn.commit()
    conn.close()