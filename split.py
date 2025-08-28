import numpy as np

arr=np.array([1,2,3,4,5,6])
ar=np.array_split(arr,2)
print(ar)

#[array([1, 2, 3]), array([4, 5, 6])]

arr2=np.array([[1,2],[3,4],[5,6]])
ar2=np.array_split(arr2,3)
print(ar2)

#[array([[1, 2]]), array([[3, 4]]), array([[5, 6]])]

ar3=np.array_split(arr2,3,axis=1)
print(ar3)

#[array([[1],
#       [3],
#       [5]]), array([[2],
#       [4],
#       [6]]), array([], shape=(3, 0), dtype=int32)]