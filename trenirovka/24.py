f = open('24.txt')
cnt1 = 0
cnt2 = 0
for i in range(1,1000):
    if 'NE'*i in f:
        cnt1+= 1

