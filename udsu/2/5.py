r = int(input())
n = int(input())
a = [1, 5, 3, 5, 6, 3, 1, 5, 7, 8, 2, 3, 6, 8, 9, 8, 1, 2,
     4, 5, 1, 5, 1, 4, 5, 4, 5, 6, 7, 11, 23,
     523, 53, 45, 34, 3,
     123, 3, 12, 12, 3, 312, 312, 55, 23,
     14, 5, 23, 643, 2, 34, 53,
     12, 4, 3, 24, 52, 525, 12]
min_digit = abs(r - (a[0] + a[1]))
i_min = 1
for i in range(2, n):
    d_tmp = abs(r - (a[i - 1] + a[i]))
    if min_digit > d_tmp:
        d_min = d_tmp
        i_min = i
print(a[i_min - 1], ",", a[i_min])
