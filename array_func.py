import numpy as np

arr=np.linspace(0,10,num=4)
print(arr)
#[ 0.          3.33333333  6.66666667 10.        ]
#diagonal arraY
#

arr=np.eye(3,5)

print(arr)
print(arr.ndim)



#[[1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]]



zeros=np.zeros(5)
print(zeros)
#[0. 0. 0. 0. 0.]
ones=np.ones(5)
print(ones)
#[1. 1. 1. 1. 1.]
mat_zeros=np.zeros((3,5))

print(mat_zeros)



#[[0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0.]]

empty=np.empty(5)
print(empty)

#[1. 1. 1. 1. 1.]

array_range=np.arange(5)
print(array_range)

#[0 1 2 3 4]