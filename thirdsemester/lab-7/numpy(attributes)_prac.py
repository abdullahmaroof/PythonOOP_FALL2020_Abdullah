import numpy as np
print("We will check dimensional of array by using ndim")
onedarr = np.array([1,2,3])
print("dimension of",onedarr," : ",onedarr.ndim)
twodarr = np.array((([1,2,3],[4,5,6],[8,7,9])))
print("dimension of",twodarr," : ",twodarr.ndim)
threedarr = np.array((([1,3,5,7,8],[4,6,9,10,2]),([1,2,3,4,8],[3,0,11,7,4])))
print("dimension of",threedarr," : ",threedarr.ndim)


print("\n\nWe will check shape of array by using shape, it will tell us the order")
onedarr = np.array([1,2,3])
print("shape of 1d array: ",onedarr," : ",onedarr.shape)
twodarr = np.array((([1,2,3],[4,5,6],[8,7,9])))
print("shape of 2d array: ",twodarr," : ",twodarr.shape)
threedarr = np.array((([1,3,5,7,8],[4,6,9,10,2]),([1,2,3,4,8],[3,0,11,7,4])))
print("shape of 3d array: ",threedarr," : ",threedarr.shape)


print("\n\nWe will check element no of array by using size, it will tell us the element")
onedarr = np.array([1,2,3])
print("elements of 1d array: ",onedarr," : ",onedarr.size)
twodarr = np.array((([1,2,3],[4,5,6],[8,7,9])))
print("elements of 2d array: ",twodarr," : ",twodarr.size)
threedarr = np.array((([1,3,5,7,8],[4,6,9,10,2]),([1,2,3,4,8],[3,0,11,7,4])))
print("elements of 3d array: ",threedarr," : ",threedarr.size)

print("\n\nWe will check datatype of array by using dtype")
onedarr = np.array([1,2,3],dtype="complex")
print("datatype of 1d array: ",onedarr," : ",onedarr.dtype)
twodarr = np.array((([1,2,3],[4,5,6],[8,7,9])),dtype="float")
print("datatype of 2d array: ",twodarr," : ",twodarr.dtype)
threedarr = np.array((([1,3,5,7,8],[4,6,9,10,2]),([1,2,3,4,8],[3,0,11,7,4])),dtype="int")
print("datatype of 3d array: ",threedarr," : ",threedarr.dtype)