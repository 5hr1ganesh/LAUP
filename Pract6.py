# Enter a matrix and check if its invertible. if the inverse exists, find the inverse

import numpy as np

M = np.array([[1, 2, 1], [2, 1, 0], [3, 0, 2]])
print("The Matrix M is:", M)
a = np.linalg.det(M)
print("Determinant of matrix M is", a)
if a <= 0:
    Minv = np.linalg.inv(M)
    print("The inverse of matrix M is", Minv)
else:
    print("Matrix is not invertible")
