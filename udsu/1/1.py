firstArray = [1,2,3,4,5,6,7,8,9,10]
secondArray = [11,12,13,14,15,16,17,18,19,20]
resultArray = []
# for i in range(1,10):
#     firstArray[i] = int(input())
#
# for i in range(1,10):
#     secondArray[i] = int(input())
# resultArray[9] = secondArray[8]
for i in range(9):
    if i%2 == 0:
        resultArray.append(firstArray[i+1])
        resultArray.append(secondArray[i-1])
print(resultArray)