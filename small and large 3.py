a = float(input("Enter your first number : "))
b = float(input("Enter your second number : "))
c = float(input("Enter your third number : "))

if(a>=b and a>=c):
    print(" Largest : ",a)
    if(b<=c):
        print("Smallest is : ",b)
    else:
        print("Smallest is : ",c)
elif(b>=a and b>=c):
    print("Largerst is : ",b )
    if(a<=c):
        print("Smallest is : ",a)
    else:
        print("Smallest is : ",c)
elif(c>=a and c>=b):
    print("Largest is : ",c)
    if(b<=a):
        print("Smallest is : ",b)
    else:
        print("Smallest is : ",a)
else:
    print("Something went wrong")