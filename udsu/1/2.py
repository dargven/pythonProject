array = [2, 3, 4, 5, 4, 3, 2, 4, 5, 3, 32, 5, 343, 2]
average_Value = sum(array) / len(array)  # считаем ср.арифм
cnt = 0
for i in range(len(array)):
    if array[i] > average_Value:
        cnt += 1
procent = cnt / len(array) * 100
print(procent, '%')
# Задан целочисленный массив. Определить процентное содержание
# элементов, превышающих среднеарифметическое всех элементов массива.
