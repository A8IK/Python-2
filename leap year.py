x = int(input("Enter your year : "))

if(x%4==0 and x%100!=0 or x%400==0):
    print(x," Is a leap year")
else:
    print(x,"Not a leap year")
