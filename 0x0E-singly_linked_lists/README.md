# Singly Linked Lists
In a normal list/array, elements are ordered/indexed with a number.

A linked list is a structure that consists of nodes and each node has a value and a pointer to another node or null.

It contains Head, Tail and Length property. The head is the beginning of the linked list and the tail is the end.

There are no indexes in a linked list.

The term ```Singly Linked List``` is because each node is connected one way to the next node unlike in ```doubly linked lists``` where there is a bidirectional connection.

## Comparing linked lists and lists/arrays

### Linked lists
- Do not have indexes
- Connected via nodes with a next pointer.
- Random access is not allowed

### Lists/Arrays
- Indexed in order
- Insertion and deletion can be expensive
- Can quickly be accessed at a specific index.

## Representation of a node
A node should have a value and a pointer to the next node, for now, the pointer to the next node is node:

Here is the representation of the node in code:

```python
class Node:
    """Node of a singly linked list"""
    def __init__(self, value: any):
        self.value = value
        self.next = None
```

## Representation of a singly linked list
A singly linked list needs a head (of type node), a tail (of type node) and a length property.

Here is the representation in code:

```python
class SinglyLinkedList:
    def __init__(self):
        self.length: int = 0
        self.head: Node = None
        self.tail: Node = None
```

## Methods on a singly linked list

### Pushing
Adding a new node to the end of the linked list

#### Pushing pseudocode
1. Write a function that accepts a value
1. Create a new node using the value passed into the function.
1. If there is no head property on the list, set the head and the tail to be the newly created node.
1. Otherwise, set the next property on the tail to be the newly created node and set the new node to be the new tail of the list.
1. Increment the length by one
1. Return the list.

Here goes the code snippet for pushing
```python
def push(self, value) -> None:
        """Adds an element at the end of a list"""
        new_node: Node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self
```


### Popping
Removing a node from the end of the list/removing the current tail of the list and set the node before it to be the tail.

#### Popping pseudocode
1. Create a function, does not take in any parameter.
1. If there are no elements in the list, return undefined.
1. Loop through the entire list until you reach the tail.
1. Set the next property of the second to last node to be null.
1. Set the tail to be the second to last node.
1. Decrement the length of the list by 1
1. If you decrement the length and it falls to zero, it means the list is empty but your code won't catch this, manually set the head and tail to be None.
1. Return the node that was removed

Here goes the code snippet
```python
    def pop(self) -> Node:
        """Removes the last node of a list"""
        if not self.head or self.length == 0:
            return None
        old_tail: Node = self.tail
        current: Node = self.head
        previous: Node = self.head
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return old_tail 
```

### Shifting
Removing a new node from the beginning of the list.

#### shifting pseudocode
1. If there are no nodes, return undefined
1. Store the current head in a variable to return it later and also to use it later in the function.
1. Set the head property to be the current head's next property.
1. Decrement the length by 1.
1. Return the node removed.

Here goes the code snippet for shifting
```python
    def shift(self) -> Node:
        """Removes the first node of a linked list"""
        if not self.head or self.length == 0:
            return None
        old_head = self.head
        self.head = old_head.next
        old_head.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return old_head
```

### Unshifting
Adding a new node to the beginning of the list

#### Unshifting pseudocode
1. Define a function that accepts a value.
1. Create a new node using the value passed to the function.
1. If there is no head property on the list, set the head and tail to be the newly created node.
1. Otherwise, set the newly created node's next property to be the current head property on the list.
1. Set the head property on the list to be that newly created node.
1. Increment the length of the list by 1.
1. Return the linked list.

Here goes the code snippet for unshift
```python
    def unshift(self, value: any):
        """Adds a new node at the beginning of the list"""
        new_node: Node = Node(value)
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
```

### Get
- Retrieving a node by it's position in the linked list.

#### Get pseudocode
1. The function should accept an index.
1. If the index is less than zero or greater than equal to length, return None.
1. Loop through the list until you reach the index and return the node at that specific index.

Here goes the code snippet for get
```python
    def get(self, index: int) -> Node:
        """Retrieves a node from a list based of a value"""
        if index < 0 or index >= self.length:
            return None
        count: int = 0
        current: Node = self.head
        while count < index:
            current = current.next
            count += 1
        return current
```

### Set
Changing the value of a node based on it's position in the linked list.

#### Set pseudocode
1. Create a function that accepts a value and an index
1. Use the get function to find the specific node.
1. If the node is not found, return false.
1. If the node is found, set the value of that node to be the value passed into the function and return true.

Here goes the code snippet for set
```python
    def set(self, index: int, value: any) -> bool:
        """Changes the value of a specific node in a list"""
        node: Node = self.get(index)
        if not node:
            return False
        node.value = value
        return True
```

### Insert
Adding a node to the linked list at a specific position.

#### Insert pseudocode
1. If the index is less than zero or greater than the length, return false.
1. If the index is the same as the length, push a new node to the end of the list.
1. If the index is zero, unshift a new node to the start of the list.
1. Otherwise, use the get method to access the node at index - 1.
1. Set the next property of that node to be the new node.
1. Connect the new node to what the node above was pointing to.
1. Increment the length  and return true.

Here goes the code snippet for insert
```python
    def insert(self, index: int, value: any):
        """Inserts a node to a specific position"""
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.push(value)
        if index == 0:
            return self.unshift(value)
        
        new_node: Node = Node(value)
        previous_node: Node = self.get(index - 1)
        temp: Node = previous_node.next
        previous_node.next = new_node
        new_node.next = temp
        self.length += 1
        return True
```

### Remove
Removing a node from the linked list at a specific position.

#### Remove pseudocode
1. If the index is less than 0 or greater than the length, return undefined.
1. If the index is the same as length - 1, pop.
1. If the index is zero, use the shift method.
1. Otherwise, using the get method, access the node at index -1.
1. Set the next property on that node to be the next of the next node.
1. Decrement the length.
1. Return the removed node.

Here goes the code snippet for removing
```python
    def remove(self, index) -> Node:
        """Removes a node from the list at a specific position"""
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.shift()
        
        previous_node: Node = self.get(index - 1)
        node_to_remove: Node = self.get(index)
        next_node: Node = self.get(index + 1)

        node_to_remove.next = None
        previous_node.next = next_node
        return node_to_remove
```

## Big O of singly linked lists
- Insertion - O(1)
- Removal - Can be O(1) or O(N), removing at the beginning is O(1)
- Searching - O(N)
- Accessing - O(N)
