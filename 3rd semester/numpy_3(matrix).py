import numpy as np

arr1 = np.arange(25).reshape(5,5)
print(arr1)
print("Taking Transpose of matrix")
arr2 = arr1.transpose()
print(arr2)
print("dot product:")
arr3 = np.dot(arr1,arr2)
print(arr3)
print("element wise square of arr1: ")
arr4 = arr1 * arr1
print(arr4)



