                ##**Method Resoulation Order(MRO)**##

class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature 1-B is working")

#For experiment only this feature.But it's very helpfull to understand

    def feature(self):
        super().__init__()



class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C init")

    def feature4(self):
        print('Feature 4 is working')

#To represent super class we use super method

    def  feat(self):
       super().feature2()

a1=C()

#For experiment feature
a2=B()

a1.feat()

#For experiment feature
a2.feature()