import numpy as np

matrA = []
matrB = []
n = int(input())
for i in range(n):
    matrA.append(list(map(int, input().split())))
if np.amax(matrA) > abs(np.amin(matrA)):
    maxes = np.amax(matrA)
else:
    maxes = abs(np.amin(matrA))#вдруг среди отрицательных будет большее число, проверяем
<<<<<<< HEAD
matrB = matrA;
=======
matrB = matrA
>>>>>>> afce27b (Initial commit)
for i in range(len(matrA)):
    for j in range(len(matrA[i])):
        matrB[i][j] = round(matrA[i][j] / abs(maxes))
print(matrB)
# Дана целочисленная матрица размера 5х5. Получить новую матрицу путем деления всех элементов данной матрицы на
# ее наибольший по модулю элемент (результаты округляем до целого числа).
