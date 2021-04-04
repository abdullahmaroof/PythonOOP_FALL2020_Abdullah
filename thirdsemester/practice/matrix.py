import numpy as np

print("Make a matrix")
row = int(input("1: Enter number of rows: "))
column = int(input("1: Enter number of columns: "))
no = row*column
matrix = np.arange(no)
for i in range(no):
    value = int(input("Enter a value in matrix at index :"))
    matrix[i] = value
matrix = matrix.reshape(row,column)
print(matrix)