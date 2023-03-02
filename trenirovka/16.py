from functools import *
@lru_cache()
def ch(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n = n//10
    return summ
@lru_cache()
def f(n):
    if n < 3:
        return 1
    if n > 2 and ch(n) % 2 !=0:
        return f(n-1) - f(n-2)
    if n > 2 and ch(n)%2 == 0:
        return f(n-1) + f(n//2)
print(f(100))