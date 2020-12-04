import cmath
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter your value of c : "))

x = (b*b)-4*a*c
if(x<0):
    print("x = ",-b/(2*a),"+",cmath.sqrt(-x)/(2*a),"i")
    print("x = ",-b/(2*a),"-",cmath.sqrt(-x)/(2*a),"i")

else:
    print("x = ",- b/(2*a)+cmath.sqrt(x)/(2*a))
    print("x = ",- b/(2*a)-cmath.sqrt(x)/(2*a))
