# Tree Traversal
Visiting every node of a tree one time.  
There are 2 main approaches to traversing a tree:
- Breath-first Search
- Depth-first Search
    - PreOrder traversal
    - InOrder traversal
    - PostOrder traversal

We will use this tree throughout this tutorial:  
```python
#      10
#   5      13
# 2   7   11   16
```
## Breadth First Traversal/Search
visits the parent first then the children.

### Breadth First Search Algorithm - iteratively
1. If the tree is empty, return None.
1. Create a queue to store nodes, this could be a list and another queue to store the values of the nodes visited.
1. Place the root node in the queue.
1. Loop as long as there is anything in the queue that stores the nodes:
    1. Dequeue a node from the queue and push the value of the node into the variable that stores the values of the nodes visited.
    1. If there is a left property on the node dequeued, add it to the queue
    1. If there is a right property on the node dequeued, add it to the queue.
1. Return the list that stores all of the visited values.

If done correctly, the output from our tree above should be:
```python
[10, 5, 13, 2, 7, 11, 16]
```

```python
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
```

## Depth First Search
These algorithms visit the nodes vertically down to the end of the tree before visiting the sibling nodes.

### PreOrder traversal
Visit the node first, then visit the entire left and then visit the entire right.

#### PreOrder traversal algorithm (recursively)
1. If the tree is empty, return None.
1. Create a list to store the values visited.
1. Store the root of the tree in a variable called current.
1. Write a function which accepts a node:
    1. Push the value of the node to the variable that stores the values.
    1. If the node has a left property, call the helper function with the left property on the node.
    1. If the node has a right property, call the helper function with the right property on the node.
1. Invoke the helper function with the current variable.
1. Return the list that stores the visited values.

If the code is implemented correctly, PreOrder traversal should produce this output on our tree:  
```python
[10, 5, 2, 7, 13, 11, 16]
```

```python
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
```

### PostOrder traversal
Visit the children then the parent.  
Visit the left child, then the right child and then the parent.  
**Post** - visit node AFTER/POST children.

#### PostOrder traversal algorithm (recursively)
1. If the tree is empty, return None.
1. Create a list to store the values of the nodes visited.
1. Store the root of the BST in a variable called current.
1. Write a helper function which accepts a node.
    1. If the node has a left property, call the helper function with the left property on the node.
    1. If the node has a right property, call the helper function with the right property on the node.
    1. Push the value of the node to the variable that stores the values.
    1. Invoke the helper function with the current variable.
1. Return the list that stores the values of the nodes visited.

If the algorithm is implemented correctly, a post order traversal on our tree should produce the following results:

```python
[2, 7, 5, 11, 16, 13, 10]
```

```python
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
```

### InOrder traversal
Visit the entire left side, then visit the node then visit the entire right side.  
InOrder traversal of a binary search tree brings out the nodes in a sorted order.

#### InOrder traversal algorithm (recursively)
1. If the tree is empty, return None
1. Store the root of the bst in a variable called current
1. Create a list to store the values of the nodes visited
1. Write a helper function which accepts a node:
    1. If the node has a left property, call the helper function with the node.
    1. Push the value of the node to the variable that stores the values.
    1. If the node has a right property, call the helper function with the right property on the node.
1. Invoke the helper function with the current variable.
1. Return the list that stores the values of the nodes visited

If the algorithm is implemented correctly, an InOrder traversal on our tree should produce the following results:
[2, 7, 5, 11, 16, 13, 10]

```python
[2, 5, 7, 10, 11, 13, 16]
```

```python
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
```

## When to use Breadth First Search or Depth First Search
- If the tree is well balanced with lots of nodes spread out - use Depth First Search. This is because, using a queue to store all these nodes would take up a lot of space.
- If there are fewer nodes to keep track of, use Breadth first approach.