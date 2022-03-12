import numpy as np

M = np.array([[1, 1, 2],
              [2, 6, 7],
              [3, 6, 7]])

T = np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])

print(T)

for i in range(len(M)):
    for j in range(len(M[0])):
        T[j][i] = M[i][j]

print(T)
