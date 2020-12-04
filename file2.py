f = open ('my info.py','r')

f1 = open ('abc','w')
##If we use 'w' in place in 'a' then it will work append that means it'll work like add something in 'abc' file
##'w' means write the file...
#f1.write('Mobile')

for data in f:
    f1.write(data)
    print(data) ##It'll print all the information from 'my info'...

#'for data' in 'abc' file we got all the  information form 'my info'