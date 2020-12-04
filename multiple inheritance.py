#Here 'class A' and 'class B' is two differents classes

class A:
    def Feature1(self):
        print("Feature 1 is working")

    def Feature2(self):
        print("Feature 2 is working")

#We are not doing here B(A) beacuse of we want to create a multiple inheritence in "class C"

class B:
    def Feature3(self):
        print("Feature 3 is working")

    def Feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def Feature5(self):
        print("Feature 5 is working")

    def Feature6(self):
        print("Feature 6 is working")



c1=C()


c1.Feature1()
c1.Feature2()

c1.Feature3()
c1.Feature4()

c1.Feature5()
c1.Feature6()



