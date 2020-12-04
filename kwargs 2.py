def person(name,**data):

    print(name)

    for i,j in data.items():
            print(i,j)

person(name='ATIK',age='18',city='DHAKA',mobail_number='01791894361')