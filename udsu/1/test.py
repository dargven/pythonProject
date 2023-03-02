n, m = map(int, input().split())
c = 0
l = 0
a = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m+n-1):#3
    for j in range(n):#2
        if ((i-j) > -1) and ((i-j) < m):
            a[j][i-j]+=c
            l+=1
            c+=1
    l = 0
for o in a:
  for o2 in o:
    print(str(o2).rjust(4), end = '')
  print()