import numpy as np


arr=np.array([1,2,3,4,5,6,7])
np.random.shuffle(arr)
print(arr)

#[4 3 1 5 7 6 2]

arr2=np.array([1,1,2,2,2,3,1,4,5,6,7,7,7,8,8,8,9,9,1,5])
x=np.unique(arr2)
print(x)
#[1 2 3 4 5 6 7 8 9]
y=np.unique(arr2,return_index=True,return_counts=True)
print(y)
#(array([1, 2, 3, 4, 5, 6, 7, 8, 9]), array([ 0,  2,  5,  7,  8,  9, 10, 13, 16], dtype=int64), 
# array([4, 3, 1, 1, 2, 1, 3, 3, 2], dtype=int64))

arr3=np.array([1,2,3,4,5,6])
print(np.resize(arr3,(2,3)))

#[[1 2 3]
# [4 5 1]]

print(np.resize(arr3,(3,2)))

#[[1 2]
# [3 4]
# [5 6]]
