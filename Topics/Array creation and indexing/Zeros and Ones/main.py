import numpy as np

import numpy as np
import statistics
data = [17,1,3,8,46,11,4,14,15,22,24,3,26,13]
Q = statistics.quantiles(data, n=4, method='inclusive')
data = np.arange(1,201)
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
Q = statistics.quantiles(data, n=4, method='inclusive')
print(Q)
IQR = Q[2]-Q[0]
upper=Q[2]+1.5*IQR
lower=Q[0]-1.5*IQR
print(94.74-228.83)
print(lower,upper)
#then upper=Q[2]+1.5*IQR and lower=Q[0]-1.5*IQR and examine sorted(data)
print(sorted(data))
print(len(data),17/4)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
if arr2d.shape == (4,3):
    print(arr2d[:2, 1:])
else:
    print(arr2d[-2:, :2])

a = int(input())
b = int(input())
print(np.ones((a,a))*b)
