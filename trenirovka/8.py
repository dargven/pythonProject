from itertools import *
cnt = 0
for i in product('012345',repeat = 6):
    s = ''.join(i)
    if s[0] != '0' and int(s) % 2 == 0 and int(s) %4 != 0:
        cnt+=1
        print(s)
print(cnt)