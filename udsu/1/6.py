import math
n = int(input())
m = int(input())
e = math.e
matr = [[0]*m]
for i in range(len(matr)):
    for j in range(matr[i]):
        matr[i][j] = (i%2?:(i+1)*n-j:k)