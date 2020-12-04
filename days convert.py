d = int(input("Enter your counting days here : "))

y = int(d/365)
d = d%365
m = int(d/30)
d = d%30


##dy = d%30


print(y," Years , ",m," Months , ",d," Days")