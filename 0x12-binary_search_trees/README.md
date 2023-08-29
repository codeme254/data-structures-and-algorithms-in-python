# Tree data structures
What is a tree? A tree is a data structure that consists of nodes in a parent/child relationship.  
They are nonlinear data structures, i.e, there is no one path, you can take several paths to a certain node unlike linked lists where we only have one path.  
A node can only point to a child, parent/child relationship, we can't have a child pointing to a parent or a child pointing to a child (sibling).

## Tree Terminology
- **Root** - the top node of a tree
- **child** - A node directly connected to another node when moving away from the root.
- **Parent** - the converse notion of a child.
- **Siblings** - nodes that have the same parents.
- **Leaf** - node that has no children.
- **Edge** - the connection between one node and another.

## Applications of trees
- HTML DOM
- Network routing
- Abstract syntax trees in programming languages
- Artificial intelligence
- Folders in operating systems.

## Types of Trees
Trees  - Nodes have any number of children.  
Binary Trees  - Each node can have at most 2 children.  
Binary Search Trees - Each node can have at most 2 children only that all the children to the left of a node are less than the node and all children to the right of the node are greater than it.

## Binary Search tree/ordered/sorted binary trees
Given a node x, all nodes to the left of x are less than it and all nodes to the right of x are greater than it.  
Every node in a binary search tree can have at most 2 children.

### The node class
```python
class Node:
    """Node of a binary search tree"""
    def __init__(self, value: any):
        self.value: any = value
        self.left: Node = None
        self.right: Node = None
```

### The binary search tree class
```python
class BinarySearchTree:
    """Binary search tree"""
    def __init__(self):
        self.root: Node = None
```

### Insert
1. Create a function that takes in a value
1. Create a new node using the value passed into the function.
1. Check if there is a root, if not, the new node becomes the root.
1. If there is a root, check the value of the new node if it is greater than or less tan the value of the root.
1. If it is greater:
    1. Check to see if there is a node to the right.
        1. If there is, move to that node and repeat these steps.
        1. If there is none, add that node as the right property.
1. If it is less:
    1. Check to see if there is a node to the left.
        1. If there is, move to that node and repeat these steps.
        1. If there is not, add that node as the left property.
1. If they are equal, don't insert the value, (you can insert it) but not inserting similar values makes it so that our binary search tree can be used to implement a set.
1. You can return the whole tree or return the inserted node.

```python
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
```

### Finding
- This is just searching for a value in the bst.
1. Create a function that takes in the value to be searched.
1. If the tree is empty, return None/False, really, any falsy value.
1. Starting at the root:
    1. Check if there is a root, if not, we are done searching.
    1. If there is a root, check if the value of the new node is the value we are looking for, if we found it we are don.
    1. If not, check to see if the value is greater than or less than the value of the root.
    1. If it is greater:
        1. Check to see if there is a node to the right.
        1. If there is, move to that node and repeat these steps.
        1. If there is not, we are done searching.
    1. If it is less:
        1. Check to see if there is a node to the left.
        1. If there is, move to that node and repeat the steps.
        1. If there is not, we are done searching.
1. If you found the node, return True, otherwise, return False.

```python
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
```

## Big O of Binary Search Trees
- Insertion - O(log n)
- Searching - O(log n)