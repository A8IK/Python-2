x = float(input("Enter your x value : "))
y = float(input("Enter your y value : "))

if(x>0 and y>0):
    print("1st quadrant")
elif(x>0 and y<0):
    print("2nd quadrinate")
elif(x==0 and y == 0):
    print("Origin")
elif(x<0 and y<0):
    print("3rd quadrant")
elif(x<0 and y==0 ):
    print("X-axis")
elif(x == 0 and y>0):
    print("Y-axis")
else:
    print("404::ERROR ")