class Node:

    def __init__(self,value):
        self.prev = None
        self.next = None
        self.val = value


class DoubleLinkedList:

     def __init__(self):
           self.head = None
           self.tail = None
           self.size = 0

     def  add (self, val):
              node = Node(val)
              if self.tail is None:
                    self.head = node
                    node.prev = self.head
                    self.tail = node
                    self.size += 1

              else:
                  self.tail.next = node
                  node.prev = self.tail
                  self.tail = node
                  self.size += 1

##Here we are updating node from 'remove'...And also we are checking here node is head or tail


     def __remove_node(self,node):

          if node.prev is None:             ##Chcking head
               self.head = node.next

          else:
              node.prev.next = node.next        ##Here we are remove node and connect to next node after remove node..


          if node.next is None:             ##Checking tail also we are taking it previous node from last node..
               self.tail = node.prev

          else:
              node.next.prev = node.prev         ##Here we are remove node and connect to prev node from remove node.



          self.size -=1



     def remove(self,value):                ##We remove 't' here (from algorithm) ..
          node = self.head                ##We can take it tail here because it is double liked list

          while node is not None:

               if node.val == value:            ##Here we are removing value which is same like passing value
                    self.__remove_node(node)   ##We are passing node and remove the value

                    #break                  ** If we use break here then it'll remove only one item from remove list..

               node = node.next         ##We are updating node here  next and next.(Why we check everytime first node??)

     def remove_first(self):
         if self.head is not None:
             self.__remove_node(self.head)


     def remove_last(self):
         if self.tail is not None:
             self.__remove_node(self.tail)

     def front(self):           ##For checking first value
         return self.head.val


     def back(self):                ##For checking last value
         return self.tail.val


     def __str__(self):
            vals = []

            node = self.head
            while node is not None:
                vals.append (node.val)
                node = node.next

            return f"[{', '.join(str(val)for val in vals)}]"

