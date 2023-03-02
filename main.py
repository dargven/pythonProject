q = list(range(18,37))
p = list(range(15,29))
a = []
for x in range(1,1000):
    if (((not(x in a)) and (x in q)) <= (x in p)):
        a.append(x)
print(a)