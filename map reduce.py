from functools import reduce

numbs=[3,2,6,8,9,4,6,2,9]
evens=list(filter(lambda n:n%2==0,numbs))
doubles=list(map(lambda n:n*2,evens))

print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)