import numpy as np

arr=np.array([1,2,3,5])
x=arr.copy()
print(arr)
print(x)


y=arr.view()
print(y)

#though copy and view quite looks the same but the difference is :
# if you change in the copy variable the data does not change in the main array
#but if you change in the view variable the main array data changes

x[0]=99
print(arr)
#[1 2 3 5]

y[0]=99
print(arr)
#[99  2  3  5]