import random
x1,y1,x2,y2 = [random.randrange(1, 9) for i in range(0,4)]
c = (x1 == x2) or (y1 == y2) or (abs(x1-x2) == abs(y1-y2))
print("The 1st field:")
print("x1: ", x1)
print("y1: ", y1)
print()
print("The 2nd field:")
print("x2: ", x2)
print("y2: ", y2)
print()
print("Queen can move in one turn from one field to another: ",c)