import numpy as np

arr=np.array([[[1,2,3],[4,5,6]]])

for i in np.nditer(arr):
    print(i)

#1
#2
#3
#4
#5
#6


for i in np.nditer(arr,flags=['buffered'],op_dtypes='S'):
    print(i)

#b'1'
#b'2'
#b'3'
#b'4'
#b'5'
#b'6'


for i,d in np.ndenumerate(arr):
    print(i,d)

#(0, 0, 0) 1
#(0, 0, 1) 2
#(0, 0, 2) 3
#(0, 1, 0) 4
#(0, 1, 1) 5
#(0, 1, 2) 6