def fib(n):
    if n <= 2:
        return 1
    fk1, fk2, fk = 1, 1, 0
    for i in range(3, n + 1):
        fk = fk2 + fk1
        fk2 = fk1
        fk1 = fk
    return fk


print(fib(1), fib(2), fib(3), fib(4), fib(5))
# Описать функцию Fib(N) целого типа, вычисляющую N-ый элемент последовательности
# чисел Фибоначчи 𝐹𝑘, которая описывается следующими формулами:
# 𝐹1=1, 𝐹2=1, 𝐹𝑘=𝐹𝑘−2+𝐹𝑘−1, k = 3, 4, …
# Используя функцию Fib, найти пять чисел Фибоначчи с данными номерами 𝑁1,𝑁2,…,𝑁5
