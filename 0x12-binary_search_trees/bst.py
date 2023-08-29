"""Implementation of a binary search tree"""

class Node:
    """Node of a binary search tree"""
    def __init__(self, value: any):
        self.value: any = value
        self.left: Node = None
        self.right: Node = None

class BinarySearchTree:
    """Binary search tree"""
    def __init__(self):
        self.root: Node = None
    
    def insert(self, value: any):
        """Adds a new node to the tree"""
        new_node: Node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        current_node: Node = self.root
        while True:
            if new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    return self
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    return self
            else:
                # if nodes are equal in value, no need to insert
                # great in implementing a set
                return self
            
    def find(self, value: any):
        """Returns True if there is a node with specified value and False if not"""
        if not self.root:
            return False
        current_node: Node = self.root
        while True:
            if current_node.value == value:
                return True
            if value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return False
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return False
    
    def dummy_view(self, node: Node):
        try:
            print(f"{node.value}")
        except AttributeError:
            print("None")

#     10
#   5     13
# 2  7  11   16
bst: BinarySearchTree = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(13)
bst.insert(2)
bst.insert(7)
bst.insert(11)
bst.insert(16)

bst.dummy_view(bst.root)
bst.dummy_view(bst.root.right)
bst.dummy_view(bst.root.left)
bst.dummy_view(bst.root.right.left)
bst.dummy_view(bst.root.right.right)
bst.dummy_view(bst.root.left.left)
bst.dummy_view(bst.root.left.right)

print(bst.find(11))