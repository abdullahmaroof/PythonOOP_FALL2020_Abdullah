import numpy as math

arr = math.array([1,3,5,7,8])
print("1d array of numpy: ")
print(arr)
print("Division 1d array of numpy with 2: ")
print(arr/2)

arr1 = math.array(([1,3,5,7,8],[4,6,9,10,2],[3,0,11,7,4]))
print("\n\n2d array of numpy: ")
print(arr1)
print("Division 2d array of numpy with 2: ")
print(arr1/2)

arr2 = math.array((([1,3,5,7,8],[4,6,9,10,2]),([1,2,3,4,8],[3,0,11,7,4])))
print("\n\n3d array of numpy: ")
print(arr2)
print("Division 3d array of numpy with 2: ")
print(arr2/2)

