x = int(input("Enter your number : "))

if(x>50 and x<100):
    if(x%13==0 or x%9==0):
        print("Yes")
    else:
        print("No")

else:
    print("Not in range")