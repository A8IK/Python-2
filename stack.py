from remove2 import DoubleLinkedList

class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()


    def push(self,val):             ##First of stack when it start when it's empty
        self.__list.add(val)

    def pop(self):                  ###Here we are throw upper element of stack

        ##All over here "decrease list size 1 and last value will return"

        val = self.__list.back()   ##When we delete value than we will not get it so we are taking it
        self.__list.remove_last()   ##Removing last value
        return val                  ##And that value will return

    def is_empty(self):              ##Here we are checking is anything here in list
        self.__list.size == 0

    def peek(self):
        return self.__list.back()


    def __len__(self):
        return self.__list.size


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.peek())
my_stack.push(5)
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(my_stack.peek())
