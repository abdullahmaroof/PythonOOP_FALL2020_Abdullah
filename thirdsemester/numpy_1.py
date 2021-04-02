import numpy as np

arr = np.array((
    [1,2,3,4,5,6],
    [2,4,6,8,10,12],
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
arr2 = arr.reshape(2,2,3)
print("Now we will print 3d array")
print(arr2)

