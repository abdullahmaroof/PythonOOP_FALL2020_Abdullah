import numpy as np

print("finding value in 1d from indexing, \npositive index start from 0, forward direction \nand negative index start from -1, reverse direction:")
onedarr = np.array([2,4,6,7,8,23,12,56,32])
print("1 D array: ",onedarr)
print("poitive index 3: ",onedarr[3])
print("negative index -4: ",onedarr[-4])

print("finding value in 2d from indexing and method is arrayname[row][column],"
      " \npositive index start from 0, forward direction coloumn and downward direction row"
      "\nand negative index start from -1, reverse direction column and upward direction row:")
twodarr = np.array(([2,4,6],[8,23,12],[56,32,43]))
print("1 D array: ",twodarr)
print("poitive index row=1,coloum=2: ",twodarr[1][2])
print("negative index row=-3,column=-1: ",twodarr[-3][-1])