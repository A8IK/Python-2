import math
for i in range(1,500):
    a = math.sqrt(i)
    if i % a == 0:
        print(i, end=' ')