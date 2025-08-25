import numpy as np


arr=np.array([1,2,3,4,5],dtype=int)
print(arr.dtype)

#int32


arr=np.array([1,2,3,4,5],dtype=np.int8)
print(arr.dtype)

#int8



arr=np.array([1,2,3,4,5],dtype='f')
print(arr)
print(arr.dtype)

#float32
#[1. 2. 3. 4. 5.]

first=np.array([1,2,3])
print(first)
print(first.dtype)


#int32

#[1 2 3]

second=np.float32(first)
print(second)
print(second.dtype)


#[1. 2. 3.]
#float32

third=np.int_(second)
print(third)
print(third.dtype)

#int32
#[1 2 3]


fourth=third.astype(float)
print(fourth)
print(fourth.dtype)