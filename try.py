
a = 5
b = 0  #If we are use here any number except 0 then it'll divid.Because except Exception is only work when try is error

try:            ##Here 'try' is special it's critical statement.It's called python - try to execute.
    print(a/b)

except Exception as e:  #"e" is representing object
##Here except work like that hey python if 'try' is error leave it to me as a programmer i'll handle it...

    print("Hey, you can't divide a number by zero" ,e)

print("Bye , Bye")