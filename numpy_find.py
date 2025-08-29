import numpy as np

arr=np.array([1,2,3,4,5,6])

find=np.where((arr/2)==2)
print(find)
#(array([3], dtype=int64),)


idx=np.searchsorted(arr,5,side="right")
print(idx)
print(arr)

#5
#[1 2 3 4 5 6]