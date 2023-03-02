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
