def Del(n,m):
    return n % m == 0
for a in range(1,1000):
    if all((a<77) and ((not(Del(x,a))) <= (Del(x,10) <=(not(Del(x,28))))) for x in range(1,1000)):
        print(a)