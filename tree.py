##It's not complete y  et


from fifoque import Queue
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class BianryTree:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root is None:
            self.root = TreeNode(val)

        else:
            nodes = Queue()
            nodes.enqueue((self.root))


        while True:
            checking node = nodes.deque()
            if checking_node.left is None:
                checking_node.left = TreeNode(val)
                return

            elif checking_node.right is None:
                nodes.enqueue(checking_node.left)
                nodes.enqueue(checking_node.right)

            else:
                nodes.enqueue(checking_node.left)
                nodes.enqueue(checking_node.right)


    def __str__(self):
        tree_printer = BianryTreePrinter()





