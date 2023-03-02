for i in range(1,100000):
    x = i
    s = 1
    a = 12
    while x // 7 > 0:
        if x % 7 < 5:
            s = s + a
        else:
            s = s +(x%7)
        x = x // 7
    if s > 42:
        print(i)