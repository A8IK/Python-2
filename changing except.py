
a = 5
b = 2


try:
    print("Resource Start")
    print(a/b)
    k = int(input("Enter your number :"))
    print(k)



except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero",e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:    #It's handle all the error(ZeroDicison, ValueError here).This exception can handle all the exception
    print("Something went wrong")


finally:
    print("Resource is finally Closed")


##Different type of error have different type of name as well.
##And general is exception so exception will be top."exception" can handle everything.You can be specific

##Different type of error we have to use different except block..