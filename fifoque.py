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



class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self,val):
         self.__list.add(val)

    def deque(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def front(self):
        return self.__list.front()

    def is_empty(self):
        return self.__list.size == 0

    def __len__(self):
        return self.__list.size

#
#from collections import  deque

#my_queue.enqueue(2)
#print(len(my_queue))
#print(my_queue.front())
#my_queue.enqueue(4)
#my_queue.enqueue(6)
#my_queue.enqueue(10)
#my_queue.enqueue(111)
#print(my_queue.front())
#print(len(my_queue))
#print(my_queue.deque())
#print(my_queue.front())
#my_queue.deque()
#print(my_queue.front())

##here is problem 1st element is not showing correctly after removing


