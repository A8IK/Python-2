f = open("my info.py",'r')

#print(f)       ##If we use this we'll get other output
#print(f.read())  #If we use that code it'll print all the information from "my info"

print(f.readline(),end = "")   #But it'll print  one by one line from "my info"
##Here if we use 'end =""' then it'll create new line without any space..

print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(5),end="")  ##Here if we use any number then it'll print that line print only 5  word
