x = str(input("Enter a char or num : "))

if(x>='a' and x<='z'):
    print("Lowercase")
elif(x>='A' and x<='Z'):
    print("Uppercase")
elif(x>='!' and x<='/' or x>=':' and x<='@' or x>='[' and x<='`' or x>='(' and x<='-'):
    print("Symbol")
elif(x>='0' and x<='9'):
    print("Digit")
else:
    print("404::ERROR")
