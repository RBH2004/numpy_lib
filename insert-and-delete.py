import numpy as np

arr=np.array([1,2,3,4,5])
x=np.insert(arr,2,89)
print(x)

#[ 1  2 89  3  4  5]

x=np.insert(arr,(2,4),(89,9.8))
print(x)

#[ 1  2 89  3  4  9  5]


arr2=np.array([[1,2,3],[1,2,3]])
x=np.insert(arr2,2,6,axis=0)
print(x)

#[[1 2 3]
# [1 2 3]
# [6 6 6]]

x=np.insert(arr2,2,6,axis=1)
print(x)

#[[1 2 6 3]
# [1 2 6 3]]

