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
arr_complex = math.array([1,3,5,7,8],"complex")
print("1d array of numpy with integer datatype: ")
print("The numpy array: ",arr_complex,"  , array dataype: ",arr_complex.dtype)

print("\n\n1d array of numpy by using arange: ")
arr3 = math.arange(1,20,2,dtype="int")
print("In arange, we give starting, ending and gap  between next element of array: ")
print(arr3)
print("In arange, we can only give ending and gap  between next element of array(it is also optional): ")
arr4 = math.arange(5,dtype="float")
print(arr4)

print("\n\narray of numpy by using zeros: ")
arr5 = math.zeros([3,3])
print("in zeros, complete matrix has value zero we will give number of rows and columns")
print(arr5)

print("\n\narray of numpy by using ones: ")
arr6 = math.ones([3,3])
print("in ones, complete matrix has value zero we will give number of rows and columns")
print(arr6)

print("\n\narray of numpy by using empty: ")
arr7 = math.empty(7,dtype="int")
print("in empty, complete array has random values: ")
print(arr7)
print("In empty we can put values to:")
for i in range(8):
    arr7[i:]= i
print(arr7)

