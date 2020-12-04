print("<<<Please choose one from below>>>")
print("<<< 1.Area of a circle>>>")
print("<<< 2.Area of a rectangle>>>")
print("<<< 3.Area of a triangle>>>")
print("<<< 4.Area of a cylinder>>>")
print("<<< 5.Volume of a sphere.")
print("<<< 6.Volume of a cube>>>")

x = input("Now It's time to choose yourself : ")

if(x == 1):
    print("<<<< Area of a Circle >>>")
    r = float(input("Enter your Radious : "))
    A = 3.1416*r*r
    print("You area of circle is : ",A)
elif(x == 2):
    print("<<<< Area of a Rectangle >>>>")
    l = float(input("Enter your length : "))
    w = float(input("Enter your width : "))
    RA = l*w
    print("Your area of rectangle is : ",RA)
elif(x == 3):
    print("<<< Area of a triangle >>>")
    b = float(input("Enter your base value : "))
    ht = float(input("Enter your height : "))
    at = (ht*b)/2
    print("Your area of triangle is : ",at)
elif(x == 4):
    print("<<< Area of a Cylinder >>>")
    rc = float(input("Enter your Radious value :"))
    hc = float(input("Enter your Height value :"))
    ac = 3.1416*rc*rc*hc
    print("This is your area of cylinder :",ac)
elif(x == 5):
    print("<<< Volume of a Sphere >>>")
    rs = float(input("Enter your radious :"))
    vs = 1.33*3.1416*rs*rs*rs
    print("This is your volume of sphere : ",vs)
elif(x == 6):
    print("<<< Volume of a Cube >>>")
    ed = float(input("Enter you edge value :"))
    vcube = ed*ed*ed
    print("This is your volume of cube : ",vcube)

else:
    print("Sorry, your number is not in a range..")



