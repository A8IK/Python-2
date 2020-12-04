a=10
def something():
    global a
    a=8
    print(a)
something()

print(a)