import numpy as np

max_num = -12321
min_num = 12123314
maxi, maxj, mini, minj, p = 0, 0, 0, 0, 0
a = np.array([[1, 2, 3], [2, 5, 6], [1, 5, 4], [2, 5, 4],
              [6, 9, 4], [1, 34, 5], [2, 1, 4], [6, 6, 4],
              [1, 7, 5], [6, 1, 28], [8, 7, 7], [6, 2, 4]])
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i, j] > max_num:
            max_num = a[i, j]
            maxi = i
            maxj = j
        if a[i, j] < min_num:
            min_num = a[i, j]
            mini = i
            minj = j
    p = a[maxi, maxj]
    a[maxi, maxj] = a[mini, minj]
    a[mini,minj] = p
    max_num = -12321
    min_num = 12123314
print(a)
