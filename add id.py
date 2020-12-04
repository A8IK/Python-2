def update (x):
    print(id(x))

    x=10

    print(id(x))
    print("x=",x)

a=8

update(a)
print(id(a))
print("a",a)