import xlsxwriter as excelWriter
import cx_Oracle
import datetime

conn = cx_Oracle.connect("system/qw12er34ty56@//localhost:1521/orcl.168.0.102")
cur = conn.cursor()
oracle = """SELECT * FROM MenuData FULL OUTER JOIN BillData ON MenuData.food = BillData.food"""
cur.execute(oracle)

def exceloracleReportGeneration():
    currentDataAndTime = datetime.datetime.now()
    dateAndTime = currentDataAndTime.strftime("%Y.%m.%d-%H.%M.%S")
    excelfileName = "oraclejoin-report-" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()
    row = 0
    column = 0

    for eachRow in cur:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0
    myWorkbook.close()
    conn.commit()
    conn.close()
