class Node:
    def __init__(self,value):
        self.next = None      #Initally we will got nothing so we just let the name "None"
        self.prev = None
        self.val = value      #Every nodes keep a value so we create it...



class DoubleLinkedList:
    def __init__(self):      ##We are create empty list here..
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,val):      #We are adding nodes here...
        node=Node(val)    ##new nodes create

##To algorithm we are connecting to nodes to head and tail and at last we are adding as a none...

        if self.tail is None:
            self.head = node
            node.prev = self.head
            self.tail = node
            self.size +=  1

##Here we add another node add it with tail(in algorithm) and at last we add to it as  None

        else:
            self.tail.next = node  ##We are added new node here
            node.prev = self.tail
            self.tail=node
            self.size +=1



    def __str__(self):             ##We need to override so we use override method...
         vals=[]
         node=self.head
         while node is not None:
             vals.append(node.val)
             node=node.next

         return f"[{','.join(str(val)for val in vals)}]"




my_list=DoubleLinkedList()
my_list.add(4)
my_list.add(5)
my_list.add(9)
print(my_list)
print(my_list.size)
