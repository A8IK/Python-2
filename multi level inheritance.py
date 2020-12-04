#That method works like , "class A" is a grandparents,'class B" is a parents and 'class C' is a parents children...
#So parents children can access her/his parents and grandparents device..

class A:

    def Feature1(self):
        print("Feature 1 is working")

    def Feature2(self):
        print("Feature 2 is working")

class B(A):
        def Feature3(self):
            print("Feature 3 is working")

        def Feature4(self):
            print("Feature 4 is working")

class C:
        def Feature5(self):
            print("Feature 5 is working")

        def Feature6(self):
            print("Feature 6 is working")


a1=B()

#Here we can access to the 'class A' because 'class B' is inheritence to 'class A'




a1.Feature1()
a1.Feature2()

a1.Feature3()
a1.Feature4()
