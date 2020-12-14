import xlsxwriter as excelWriter
import datetime


dataList = [[1, "Ali", "Yunus", 45],[2,"Kamran","Latif",49, "55%"],[3,"Jamil","Rizwan",41],[4,"Hussain","Aslam",39,"30%"],[5,"Usman", "Hassan",31]]

def excelReportGeneration(x):
    currentDataAndTime = datetime.datetime.now()
    dateAndTime = currentDataAndTime.strftime("%Y.%m.%d-%H.%M.%S")
    excelfileName = "report-" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()
    row = 3
    column = 4

    for eachRow in x:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 4
    myWorkbook.close()

excelReportGeneration(dataList)

