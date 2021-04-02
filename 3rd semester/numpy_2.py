#matrix
import numpy as np

m = np.matrix('1,2,3;4,5,6;7,8,9')
print(m)
print(np.diagonal(m))
print(m.min())
print(m.max())