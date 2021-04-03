import numpy as np
print("We will check dimensional of array by using ndim")
onedarr = np.array([1,2,3])
print("dimension of",onedarr," : ",onedarr.ndim)
twodarr = np.array((([1,2,3],[4,5,6],[8,7,9])))
print("dimension of",twodarr," : ",twodarr.ndim)
threedarr = np.array((([1,3,5,7,8],[4,6,9,10,2]),([1,2,3,4,8],[3,0,11,7,4])))
print("dimension of",threedarr," : ",threedarr.ndim)