# Queues
It is a First In First Out (FIFO) data structure.  
The first element to be added into a stack should be the first element to be removed.  

## Uses
- Background tasks
- Uploading resources
- Printing/Task processing.

## Implementation of queues
- **We can use an array**
- **We can use a linked list**

### Implementing using a linked list
We only care about two methods, the first one is a method to add to the queue which we can call ```enqueue()``` and the other one is for removing from the queue which we can call ```dequeue()```.  
Every element in a queue is just a node as shown.

```python
class Node:
    """node of a queue"""
    def __init__(self, value: any):
        self.value = value
        self.next = None
```

The queue class

```python
class Queue:
    """Queue data structure"""
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.size: int = 0
```

#### Enqueue
Adding to the queue

##### Enqueue pseudocode
1. Create a function that takes in a value.
1. Create a new node using the value passed into the function.
1. If there are no nodes in the queue, set this node to be the first and the last property.
1. If there are, set the next property of the last node to point to the new node.
1. Set the new node to be the last.
1. Increment the size of the queue and return the queue.

```python
    def enqueue(self, value: any):
        """Adds a new node at the end of the queue"""
        new_node: Node = Node(value)
        if not self.first or self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self
```

#### Dequeue
Removing a node from the queue, (at the beginning).

##### Dequeue pseudocode
1. If there are no nodes, return None.
1. Store the first property in a variable.
1. If there is only one node in the list, set the first and the last to be None.
1. If there is more than one node, set the first property to be the next property of first.
1. Decrement the size by 1.
1. Return the value of the node dequeued.

```python
    def dequeue(self):
        """Removes a node at the beginning of the queue"""
        if not self.first or self.size == 0:
            return None
        current_first: Node = self.first
        if self.size == 0:
            self.first = None
            self.last = None
        else:
            self.first = current_first.next
            current_first.next = None
        self.size -= 1
        return current_first
```

## Big O of queues
Insertion - O(1)  
Removal - O(1)  
Searching - O(N)  
Access - O(N)  
