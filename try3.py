

a = 5
b = 2

k = int(input("Enter a Number :"))
print(k)
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number :"))
    print(k)

except Exception as e:  #value is the part of exception.exception can handle everything.But you have to specific
    print("Hey, You can not divided Number by zero",e)

##Here "e" is specificly print why it is error..We can use other literal


finally:
    print("Resource is finally closed")
