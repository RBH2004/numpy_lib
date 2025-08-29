import numpy as np

arr=np.array([1,8,3,4,5,6])

find=np.where((arr/2)==2)
print(find)
#(array([3], dtype=int64),)


idx=np.searchsorted(arr,5,side="right")
print(idx)
print(arr)

#5
#[1 8 3 4 5 6]

arr=np.sort(arr)
print(arr)
#[1 3 4 5 6 8]


#filtering

array=np.array([7,8,9,1])
f=[False,True,False,True]
print(array[f])

#[8 1]