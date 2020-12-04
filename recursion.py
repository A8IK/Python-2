import sys
sys.setrecursionlimit(2500)
print(sys.getrecursionlimit())
i=4
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()
greet()

