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

print("\n\nArray of numpy by using datatype")
arr_int = math.array([1,3,5,7,8],"int")
print("1d array of numpy with integer datatype: ")
print("The numpy array: ",arr_int,"  , array dataype: ",arr_int.dtype)
arr_float = math.array([1,3,5,7,8],"float")
print("1d array of numpy with integer datatype: ")
print("The numpy array: ",arr_float,"  , array dataype: ",arr_float.dtype)