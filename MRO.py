#Method Resolution Order (MRO)

class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2 (self):
        print("Feature 2 is working")


class B:
    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
#Here 'super()' is a special variable ..
# #supppose we use in here 'Class C' first it'll go to left side after go right side (such like multiple inherritance)

        super().__init__()
        print("In C init")

    def feature5(self):
        print("Feature 5n is working")


a1=C()
a1.feature1()