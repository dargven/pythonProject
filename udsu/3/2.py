import numpy

M = 7
a = numpy.zeros((M, M))
k = 0
for i in range(0, M):
    for j in range(i, M - i):
        k += 1
        a[j][i] = k
    for j in range(i + 1, M - i):
        k += 1
        a[M - 1 - i][j] = k
    for j in range(M - 2 - i, i - 1, -1):
        k += 1
        a[j][M - 1 - i] = k
    for j in range(M - 2 - i, i, -1):
        k += 1
        a[i][j] = k
    i += 2
print(a)
