import numpy as np
matrA = []
matrB = []
n = int(input())
for i in range(n):
    matrA.append(list(map(int, input().split())))
if np.amax(matrA) > abs(np.amin(matrA)):
    maxs = np.amax(matrA)
else:
    maxs = abs(np.amin(matrA))
matrB = matrA;
for i in range(len(matrA)):
    for j in range(len(matrA[i])):
        matrB[i][j] = round(matrA[i][j]/abs(maxs))
print(matrB)