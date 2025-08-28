import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([4,5,6,7])
print(np.concatenate((arr2,arr1)))

#[4 5 6 7 1 2 3 4]

arr3=np.array([[1,2],[3,4]])
arr4=np.array([[5,6],[7,8]])
print(np.concatenate((arr3,arr4),axis=1))
#[[1 2 5 6]
# [3 4 7 8]]

print(np.concatenate((arr3,arr4),axis=0))
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]


#starting of stack

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

s=np.stack((arr1,arr2),axis=0)
print(s)

#[[1 2 3 4]
# [5 6 7 8]]

s=np.stack((arr1,arr2),axis=1)
print(s)

#[[1 5]
# [2 6]
# [3 7]
# [4 8]]

s1=np.hstack((arr1,arr2))
print(s1)
#[1 2 3 4 5 6 7 8]

s2=np.vstack((arr1,arr2))
print(s2)

#[[1 2 3 4]
# [5 6 7 8]]

s3=np.dstack((arr1,arr2))
print(s3)

#[[[1 5]
#  [2 6]
#  [3 7]
#  [4 8]]]


