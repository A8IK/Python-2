##Same type of age calculator or Human life calculator and also number in words try same way..

x = int(input("Enter your subject  number : "))

if(x>=85 and x<=100):
    print("Hey, you got A ")
elif(x>=80  and x<85):
    print("Hey, you got A- ")
elif(x>=75 and x<80):
    print("Hey you got B+")
elif(x>=70 and x<75):
    print("Hey, you got B")
elif(x>=65 and x<70):
    print("Hey you got B-")
elif(x>=60 and x<65):
    print("Hey you got C+")
elif(x>=55 and x<60):
    print("Hey you got C")
elif(x>=50 and x<55):
    print("Hey you got C-")
elif(x>=45 and x<50):
    print("Hey you got D+")
elif(x>=40 and x<45):
    print("Hey, you got D")
elif(x>=0 and x<40):
    print("Hey , you got F")
else:
    print("Please enter right number ")