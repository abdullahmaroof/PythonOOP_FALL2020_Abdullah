import numpy as np

print("Make a matrix")
row = int(input("1: Enter number of rows: "))
column = int(input("2: Enter number of columns: "))
no = row*column
matrix = np.arange(no)
print("\nSelect the type of matrix:")
print("1: Null Matrix")
print("2: Ones Matrix")
print("3: Matrix containing different values")
press = int(input("Press 1 - 3: "))
if press == 1:
    matrix = np.zeros([row,column],dtype="int")
    print("\n\nZero Matrix:")
    print(matrix)
elif press == 2:
    matrix = np.ones([row,column],dtype="int")
    print("\n\nOnes Matrix:")
    print(matrix)
elif press == 3:
    print("\n")
    for i in range(no):
        value = int(input("Enter a value in matrix:"))
        matrix[i] = value
    matrix = matrix.reshape(row,column)
    print("Matrix:")
    print(matrix)
else:
    print("\n\nWrong key")

