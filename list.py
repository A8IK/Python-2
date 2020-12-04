def update(lst):
    print(id(lst))

    lst[1]=22
    print(id(lst))
    print("x=",lst)

lst=[12,28,36,45]
print(id(lst))
update(lst)
print("lst=",lst)

