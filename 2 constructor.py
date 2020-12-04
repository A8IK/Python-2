class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A):

##When we use constructor in sub class then it first check 'SUB CLASS' constructor after pass to 'SUPER CLASS'..But
##If we use "__init__" function in sub class then it'll not pass to super class until we use 'SUPER CLASS"

    def __init__(self):

## Mainly when we create object of "SUB CLASS (B)" it will call init of "SUB CLASS (B)" first ..But
    ##if we have "CLASS SUPER" then it'll first call init of 'SUPER CLASS (A)" then call init of 'SUB CLASS (B)"

        super().__init__()
        print("In B init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


a1=B()