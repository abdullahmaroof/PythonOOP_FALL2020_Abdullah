import numpy as np
print("Matrix arr1")
arr1 = np.arange(25).reshape(5,5)
print(arr1)
print("\nTaking Transpose of matrix arr1: ")
arr2 = arr1.transpose()
print(arr2)
print("\ndot product of arr1 and arr2:")
arr3 = np.dot(arr1,arr2)
print(arr3)
print("\nelement wise square of arr1: ")
arr4 = arr1 * arr1
print(arr4)
