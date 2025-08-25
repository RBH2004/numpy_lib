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


random=np.random.rand(4)
print(random)

#any kind of number with range(0,1)
#for example : [0.17823633 0.84123617 0.93194898 0.89321629]


random_whole=np.random.randn(5)
print(random_whole)

#Both positive and negative numbers can be there with numbers close to 0
#For example : [-0.20677452 -1.3369497   1.20079417 -1.04331284 -0.35277995]

random_f=np.random.ranf(5)

print(random_f)

#[0.72061847 0.42650527 0.67011744 0.04146737 0.13604658]


random_range_of_int=np.random.randint(0,80,5)
print(random_range_of_int)
#function(min,max,total)
#[54 74 76 25 54]