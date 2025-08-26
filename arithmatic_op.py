import numpy as np

arr=np.array([1,2,3,4])
new_arr=arr/2

print(new_arr)

#[0.5 1.  1.5 2. ]

arr2=np.array([4,5,6,7])
arr2=arr+arr2
print(arr2)
#shape must be similar
#[ 5  7  9 11]


new_add=np.add(arr,arr2)#similar subrtact,multiply,divide,mod,power,reciprocal
#reciprocal is 1/x if x is given as a number
print(new_add)

#[ 6  9 12 15]
#2D Matrix

first=np.array([[1,2,3],[4,5,6]])
second=np.array([[1,2,3],[4,5,6]])

addition_2D=first+second
print(first+second)


reciprocal=np.reciprocal(first)
print(reciprocal)

#[[1 0 0]
# [0 0 0]]