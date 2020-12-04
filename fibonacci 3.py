def fib(n):

    a=0
    b=1
    d = 0
    e = -1
    if n<=0:

        for i in range(2,n):
            k = e+n
            d=e
            e=d


            print(k)

    elif n==1:
        print(a)
        print(b)


    else:

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(-3)


