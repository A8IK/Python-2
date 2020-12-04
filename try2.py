a = 5
b = 0

try:
    print("Resource Open")
    print(a/b)          ##This line is exception.It's jumping outside of statement
    print("Resource Close")     ##If we use zero for division then this line won't be check

except Exception as e:      ##It's only work when we divide it by zero
    print("Hey, you can't divide a Number by zero", e)

##  "e"

finally:
    print("Resource finally Closed")

# "finally" block will be executed if we get error as well as if we don't get the error,
#It doesn't matter am I expecting something or not..