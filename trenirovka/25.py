for i in range(800001,1000000):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            if (j + i//j) % 144 == 0:
                print(i, j + i//j)