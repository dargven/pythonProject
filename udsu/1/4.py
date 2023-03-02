matr = []
cnt = 0
n = int(input())
for i in range(n):
    matr.append(list(map(int, input().split())))
number = int(input())
for i in range(len(matr)):
    for j in range(len(matr[i])):
        if number == matr[i][j]:
            cnt+=1
print(cnt)