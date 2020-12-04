
f = open('IMG_2020081.jpg','rb')        #Here 'r' means reading and 'b' means binary

f1 = open('MyPic.JPG','wb')  #This line is write binary to help show the pic below the name

for i in f:
    #print(i)
    f1.write(i)



##It'll need main picture.jpg file in project file
