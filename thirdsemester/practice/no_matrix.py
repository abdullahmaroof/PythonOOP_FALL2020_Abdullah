import numpy as np

matrix = []
row = []
column = []
matrix_no = int(input("Enter no of matrix: "))
for x in range(0, matrix_no):
    print("\nMatrix no ", x + 1, ":")
    row_no = int(input("1: Enter number of rows: "))
    row.append(row_no)
    column_no = int(input("2: Enter number of columns: "))
    column.append(column_no)
    no = row_no * column_no
    array = np.arange(no)
    matrix.append(array)
for i in range(0,matrix_no):
    matrix[i] = matrix[i].reshape(row[i],column[i])
    print("\n\nMatrix no ",i+1,":")
    print(matrix[i])