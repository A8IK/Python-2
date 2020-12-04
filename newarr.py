from array import*
vals=array('i',[5,9,8,6,7])
newArr=array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)