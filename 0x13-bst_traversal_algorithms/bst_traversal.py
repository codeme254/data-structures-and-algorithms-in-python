"""Implementation and traversal of a binary search tree"""
from typing import List

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
    
    def breadth_first_traversal(self):
        """Performs breadth first traversal on a tree"""
        if not self.root:
            return None
        nodes_queue: List[Node] = []
        visited: List[any] = []
        nodes_queue.append(self.root)
        while len(nodes_queue) > 0:
            current_node: Node = nodes_queue.pop(0)
            visited.append(current_node.value)
            if current_node.left:
                nodes_queue.append(current_node.left)
            if current_node.right:
                nodes_queue.append(current_node.right)
        return visited
    
    def dfs_pre_order_traversal(self):
        """Performs depth first pre-order traversal on a tree"""
        if not self.root:
            return None
        visited: List[any] = []
        current: Node = self.root

        def traverse_helper(node: Node):
            visited.append(node.value)
            if node.left:
                traverse_helper(node.left)
            if node.right:
                traverse_helper(node.right)
        traverse_helper(current)
        return visited
    
    def dfs_post_order_traversal(self):
        """Performs post order traversal on a tree"""
        if not self.root:
            return None
        current: Node = self.root
        visited: List[any] = []

        def traverse_helper(node: Node):
            if node.left:
                traverse_helper(node.left)
            if node.right:
                traverse_helper(node.right)
            visited.append(node.value)
        traverse_helper(current)
        return visited
    
    def dfs_in_order_traversal(self):
        """Performs an InOrder traversal on a tree"""
        if not self.root:
            return None
        visited: List[any] = []
        current: Node = self.root

        def traverse_helper(node: Node):
            if node.left:
                traverse_helper(node.left)
            visited.append(node.value)
            if node.right:
                traverse_helper(node.right)
        traverse_helper(current)
        return visited
    
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

print(bst.breadth_first_traversal())
print(bst.dfs_pre_order_traversal())
print(bst.dfs_post_order_traversal())
print(bst.dfs_in_order_traversal())
print(bst.find(11))