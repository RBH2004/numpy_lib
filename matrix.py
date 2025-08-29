import numpy as np

arr=np.array([[1,2],[4,5]])
print(np.transpose(arr))

#[[1 4]
# [2 5]
# [3 6]]

print(np.swapaxes(arr,1,0))
#[[1 4]
# [2 5]
# [3 6]]

print(np.linalg.inv(arr))
#[[-1.66666667  0.66666667]
# [ 1.33333333 -0.33333333]]


print(np.linalg.matrix_power(arr,2))
#[[ 9 12]
# [24 33]]
print(np.linalg.matrix_power(arr,0))
#[[1 0]
# [0 1]]

print(np.linalg.det(arr))
#-2.9999999999999996