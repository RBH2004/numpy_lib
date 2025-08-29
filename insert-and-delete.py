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

x=np.insert(arr2,2,[22,24,26],axis=0)
print(x)

#[[ 1  2  3]
# [ 1  2  3]
# [22 24 26]]


arr3=np.array([1,2,3,4,5,6])
x=np.append(arr3,6.4)
print(x)

#[1.  2.  3.  4.  5.  6.  6.4]

arr4=np.array([[1,2,3],[4,5,6]])
y=np.append(arr4,[[22,23,24]],axis=0)
print(y)

#[[ 1  2  3]
# [ 4  5  6]
# [22 23 24]]

arr3=np.array([1,2,3,4,5,6])
x=np.delete(arr3,2)
print(x)

#[1 2 4 5 6]

