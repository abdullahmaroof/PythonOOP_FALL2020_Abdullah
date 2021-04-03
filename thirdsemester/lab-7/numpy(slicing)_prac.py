import numpy as np

print("slicing of 1 D array, method arrayname[start:end range(it must be one more value:step(optional)")
onedarr = np.array([1,3,5,7,12,34,21])
print("1 D array: ",onedarr)
print("slicing method \'[:]\' :",onedarr[:])
print("slicing method \'[2:]\' :",onedarr[2:])
print("slicing method \'[:4]\' :",onedarr[:4])
print("slicing method \'[3:6]\' :",onedarr[3:6])
print("slicing method \'[1:7:2]\' :",onedarr[1:7:2])