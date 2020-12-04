h = int(input("Enter your hour counting : "))

w =int( h/168)
h = h%168
d = int(h/24)
h = h%24

print(w," Weeks , ",d," Days , ",h," Hours")

