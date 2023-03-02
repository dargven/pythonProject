f = open('17.txt')
a = []
summ = 0
lern = 0
pari = []

for s in f:
    a.append(int(s))
    for i in range(len(a)):
        if a[i] % 2 != 0:
            summ += a[i]
            lern += 1
sr_znach = summ/lern
for i in range(len(a)-2):
    cnt = 0
    if (a[i]% 3 != a[i+1]%3 != a[i+2]%3):
        if a[i] > sr_znach:
            cnt+= 1
        if a[i+1] > sr_znach:
            cnt+= 1
        if a[i+2] > sr_znach:
            cnt += 1
    if cnt == 1:
        pari.append(a[i]+a[i+1]+a[i+2])
print(sr_znach)
print(len(pari), max(pari))