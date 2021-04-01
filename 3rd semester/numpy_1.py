import numpy as np

arr = np.array((
    [1,2,3,4,5],
    [2,4,6,8,10],
    [0,2,4,6,8],
    [1,3,5,7,9],
    [3,6,9,12,15]
))

print(arr)
print(arr.shape)
print(arr.size)
arr = arr.flatten()
print(arr)
arr1 = arr
print("after doing shallow copying")
print(id(arr))
print(id(arr1))
arr1 = arr.copy()
print("after doing deep copying")
print(id(arr))
print(id(arr1))
