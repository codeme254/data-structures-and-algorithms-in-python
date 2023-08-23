# Doubly Linked Lists
Similar to linked lists only that each node points to the next and previous node.

The head node (first node) has a previous node being None and the tail node (last node) has a next node being None.

The only tradeoff is that it takes more memory but Hey, ```More memory == More Flexibility```

## The node class
```python
class Node:
    """Node of a doubly linked list"""
    def __init__(self, value: any):
        self.value = value
        self.next = None
        self.previous = None
```

## The doubly linked list class
```python
class DoublyLinkedList:
    """Doubly linked list"""
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0
```

## Methods on a doubly linked lists
### Push
Adding a node to the end of a doubly linked list.  

#### Pushing pseudocode
1. Create a function that accepts a value.
1. Create the new node with the value passed into the function.
1. If the list is empty, set the head and the tail to be the newly created node.
1. If not, set the next property on the tail to be that node.
1. Set the previous property of the new node to be the old tail.
1. Set the tail to be the newly created node.
1. Increment the length of the list and return the entire list.

```python
    def push(self, value: any):
        """Adds a new node to the end of the list"""
        new_node: Node = Node(value)
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return self
```

### Pop
Removing a node from the end of the doubly linked list.  
In a doubly linked list, it is simpler and more efficient than in a singly linked list.

#### Pop pseudocode
1. If the list is empty, return undefined.
1. Otherwise, store the current tail in a variable to return later.
1. If the length is 1, set the head and tail to be null.
1. Update the tail to be the previous node.
1. Set the new tail's next to be null.
1. Set the old tail's previous to be null.
1. Decrement the length of the list.
1. Return the removed tail.

```python
    def pop(self):
        """Removes the last node of the list"""
        if not self.head or self.length == 0:
            return None
        old_tail: Node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.previous
            self.tail.next = None
            old_tail.previous = None
        self.length -= 1
        return old_tail
```

### Shifting
Removing a node from the beginning of a doubly linked list.

#### Shifting pseudocode
1. If the list is empty, return None.
1. Otherwise, store the current head to return it later.
1. If the length is 1, make the head and the tail to be both None.
1. Otherwise, update the head to be the next property of the old head.
1. Set the head's previous property to be None.
1. Set the old head's next property to be None.
1. Decrement the length.
1. Return the old head.

```python
    def shift(self):
        """Removes the first node of a doubly linked list"""
        if not self.head or self.length == 0:
            return None
        old_head: Node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            self.head.previous = None
            old_head.next = None
        self.length -= 1
        return self.head
```

### Unshift
Adds a node at the beginning of a doubly linked list.

#### Unshift pseudocode
1. Create a function that takes in a value.
1. Create a new node with the value passed into the function.
1. If the list is empty, set the head and the tail to be the new node.
1. Otherwise, set the previous property on the head of the list to be the new node.
1. Set the next property on the new node to be the head property.
1. Update the head to be the new node.
1. Increment the length of the list.
1. Return the list

```python
    def unshift(self, value: any):
        """Adds a new node at the beginning of a doubly linked list"""
        new_node: Node = Node(value)
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
```

### Get
Accessing a node in a doubly linked list by its position.  
Takes an index and returns the node at that index.  
It comes with an improvement in doubly linked list which can make it work at O(0.5n) which is technically O(n) but it can save the day.  
Depending on the size of the index, we can start from the beginning towards the end or from the end towards the beginning.

"Is the index closer to zero or is it closer to the end"

#### Get pseudocode.
1. Create a function that takes in an index.
1. If the index is less than 0 or is greater than or equal to the length, return None.
1. If the index is less than or equal to half the length of the list:
    1. Loop through the list starting from the head and loop towards the middle.
    1. Return the node once it is found.
1. If the index is greater than half the length of the list:
    1. Loop through the list starting from the end towards the head.
    1. Return the node once found.

```python
    def get(self, index: int):
        """Returns the node at a given index using zero based indexing"""
        if index < 0 or index >= self.length:
            return None
        mid_list: int = self.length // 2
        if index <= mid_list:
            counter: int = 0
            current: Node = self.head
            while counter != index:
                current = current.next
                counter += 1
            return current
        else:
            counter: int = self.length - 1
            current: Node = self.tail
            while counter != index:
                current = current.previous
                counter -= 1
            return current
```

### Set
Replacing the value of a node in a doubly linked list.
#### Set pseudocode
1. Create a function that takes in the index of the node to be set and the value of that node.
1. Create a variable which is the result of the get method at the index passed to the function.
1. If get method returns a valid node, set the value of that node to be the value passed to the function.
1. Return True.
1. Otherwise return false.

```python
    def set(self, index: int, value: any):
        """Replaces the value of a node in a doubly linked list"""
        node: Node = self.get(index)
        if node:
            node.value = value
            return True
        return False
```

### Insert
Adding a node in a doubly linked list by a certain position.  
It has the pain of making resetting and making too many connections.

#### Insert pseudocode
1. If the index is less than zero or greater than the length, return False.
1. If the index is 0, unshift.
1. If the index is the same as length, push.
1. Otherwise, use the get method to access the index - 1.
1. Set the next and previous properties on the correct nodes to link everything together.
1. Increment the length.
1. Return True.

```python
    def insert(self, index: int, value: any):
        """Adds a node in a doubly linked list by a certain position"""
        if index < 0 or index > self.length:
            return False
        # not not is a way of coalescing to return true
        if index == 0:
            return not not self.unshift(value)
        if index == self.length:
            return not not self.push(value)
        node_before: Node = self.get(index-1)
        new_node: Node = Node(value)
        node_after: Node = node_before.next
        node_before.next = new_node
        new_node.previous = node_before
        new_node.next = node_after
        node_after.previous = new_node
        self.length += 1
        return True
```

### Remove
Removing a node in a doubly linked list by a certain position.

#### Remove pseudocode
1. Create a function that takes in an index.
1. Check if the index is invalid, if it is less than zero or equal to the length, return None.
1. If the index is 0, shift.
1. If the index is equal to length-1, pop.
1. Use get to retrieve the item to remove.
1. Update the next and previous properties to remove the found node from the list.
1. Set the next and previous to None on the found node.
1. Decrement the length.
1. Return the removed node.

```python
    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        node_to_remove: Node = self.get(index)
        node_before: Node = node_to_remove.previous
        node_after: Node = node_to_remove.next
        node_to_remove.previous = None
        node_to_remove.next = None
        node_before.next = node_after
        node_after.previous = node_before
        self.length -= 1
        return node_to_remove
```

## Big O of doubly linked lists
Insertion - O(1)  
Removal - O(1)  
Searching - O(N)  
Access - O(N)  
