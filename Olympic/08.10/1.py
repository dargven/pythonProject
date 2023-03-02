n,m = map(int,input().split())
vsego_predmetov = []
items = str(input())
unosim = 0
items = items.split()
for i in items:
    vsego_predmetov.append(int(i))
vsego_predmetov.sort(reverse = True)
for i in range(m):
    if vsego_predmetov[i] > 0:
        unosim += vsego_predmetov[i]
print(unosim)