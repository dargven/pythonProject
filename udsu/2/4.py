n = int(input())
a = [1, 5, 3, 5, 6, 3, 1, 5, 7, 8, 2, 3, 6, 8, 9, 8, 1, 2,
     4, 5, 1, 5, 1, 4, 5, 4, 5, 6, 7, 11, 23,
     523, 53, 45, 34, 3,
     123, 3, 12, 12, 3, 312, 312, 55, 23,
     14, 5, 23, 643, 2, 34, 53,
     12, 4, 3, 24, 52, 525, 12]
min_digit = 121212112312321
number1, number2 = 0, 0
for i in range(len(a) - 1):
    if abs(a[i] - a[i + 1]) < min_digit:
        min_digit = abs(a[i] - a[i + 1])
        number1 = i
        number2 = i + 1
if number1>number2:
    print(number2,number1)
else:
    print(number1,number2)
