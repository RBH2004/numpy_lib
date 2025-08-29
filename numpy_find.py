import numpy as np

arr=np.array([1,2,3,4,5])

find=np.where((arr/2)==2)
print(find)
#(array([3], dtype=int64),)