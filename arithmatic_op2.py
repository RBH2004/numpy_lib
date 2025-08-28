import numpy as np

arr=np.array([3,2,1,4,5,6])

print(np.cumsum(arr))
#[ 3  5  6 10 15 21]
print(np.min(arr),np.argmin(arr))
#1 2
print(np.max(arr),np.argmax(arr))
#6 5
print(np.sqrt(arr))
#[1.73205081 1.41421356 1.         2.         2.23606798 2.44948974]
print(np.sin(arr))
#[ 0.14112001  0.90929743  0.84147098 -0.7568025  -0.95892427 -0.2794155 ] 
print(np.cos(arr))
#[-0.9899925  -0.41614684  0.54030231 -0.65364362  0.28366219  0.96017029] 



arr_2d=np.array([[2,1,3],[4,5,6]])

print(np.min(arr_2d,axis=0))#column wise minimum number
#[2 1 3]
print(np.max(arr_2d,axis=1))#row wise maximum number
#[3 6]

#0 for column
#1 for rows

