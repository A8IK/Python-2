
                        ##(**That's important**)##
##Sub Class can access all the features of Super Class But Super Class can not access all the features...

#Super Class A (Here)

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

#Class B is a Child class or Sub class.
#Here B(A) that's called inheritence."Class B" is inheritance from "class A"

class B(A):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


a1=A()
b1=B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()