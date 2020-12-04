a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

if(a*a+b*b==c*c):
    print("Right Triangle")

elif(a*a+c*c==b*b):
    print("Right triangle")

elif(b*b+c*c==a*a):
    print("Right triangle")

else:
    print("Not right triangle")
