##ABC = Abstract Base Class

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

#class Laptop(Computer):     ##It's got an error because Laptop class is sub class of Computer class and Computer class is in @abstractmethod
    #pass

class Laptop(Computer):     #That class implement all the method.If fail to implement then it'll error
    def process(self):
        print("It's running")

class Whiteboard:       #If we use (Computer) in Whiteboard class then it'll be an error because can't instatiate abstract class with abstract method process
    def write(self):
        print("it's writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

#com1 = Computer()
com2 = Laptop()
com3 = Whiteboard()
#com.process()


prog1 = Programmer()
prog1.work(com2)
