# Stacks
A Last In First Out data structure (LIFO).  
The last element added is the first element to be removed.  
For example, a stack of place, we add a new plate to the top and remove a plate from the top.  
The last element to be added in is the first element to be removed.

## Where stacks are used
- Managing function invocations.
- Undo/redo logic.
- Routing (the history object) is treated like a stack.

## Implementing a stack
There is more than one way of implementing a stack.  
- **Array implementation** - store data in the array such that the last thing to be added is the first thing to be removed. In this case, we only use the method of adding to the end of the array for adding and for removing, we removing from the start of the array.
- **Implementing using a linked list**

## Implementing using a linked list
We only care about creating two methods, a ```push()``` method to add to the stack and a ```pop()``` method to remove from the stack.  
Every stack element can also be treated as a node.

```python
class Node:
    """Node of a stack"""
    def __init__(self, value: any):
        self.value = value
        self.next = None
```

And here is our stack data structure
```python
class Stack:
    """Stack data structure"""
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.size: int = 0
```

### Pushing
Add a value to the top of the stack.  

##### Pushing pseudocode
1. Create a function that accepts a value.
1. Create a new node with the value.
1. If there are no nodes in the stack, make the new node to be the first and the last.
1. If there are, create a variable that stores the current first property on the stack.
1. Reset the first property to be the newly created node.
1. Set the next property on the new node to be the old head.
1. Increment the size of the stack with 1

```python
    def push(self, value: any):
        """Adds a new node to the top of the stack"""
        new_node: Node = Node(value)
        if not self.first or self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            old_first: Node = self.first
            self.first = new_node
            new_node.next = old_first
        self.size += 1
        return self
```

### Pop
Removing the first node of the stack.

#### pop pseudocode
1. If there are no nodes in the stack, return None.
1. Create a temporary variable to store the first property on the stack.
1. If there is only one node, set the first and the last property to be None.
1. If there is more than one node, set the first property to be the next property on the current first.
1. Decrement the size by 1.
1. Return the value of the removed node.

```python
    def pop(self):
        """Removes the first node of the stack"""
        if not self.first or self.size == 0:
            return None
        current_first: Node = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            self.first = current_first.next
            current_first.next = None
        self.size -= 1
        return current_first
```

## Big O of stacks
Insertion - O(1)  
Removal - O(1)  
Searching - O(N)  
Access - O(N)  