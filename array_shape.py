import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print(arr)

#[[1 2 3]
# [4 5 6]]
print(arr.shape)

#(2, 3)

arr2=np.array([1,2,3,4],ndmin=4)
print(arr2)
#[[[[1 2 3 4]]]]
print(arr2.shape)
#(1, 1, 1, 4)


arr3=np.array([1,2,3,4,5,6])
print(arr3)
#[1 2 3 4 5 6]
print(arr3.ndim)
#1
arr3=arr3.reshape(3,2)
print(arr3)
#[[1 2]
# [3 4]
# [5 6]]
print(arr3.ndim)
#2
arr3=arr3.reshape(-1)
print(arr3)
#[1 2 3 4 5 6]
print(arr3.ndim)
#1



arr4=np.array([1,2,3])
print(arr4.shape)
print(arr4)


arr5=np.array([[1],[2],[3]])
print(arr5.shape)
print(arr5)

#[[1]
# [2]
# [3]]

final=arr4+arr5
print(final)

#[[2 3 4]
# [3 4 5]
# [4 5 6]]

#when we compare the row x column of both matrix . we compare first the columns
#and then the rows together. either both columns have to be same or one of them
#has to be one. 

