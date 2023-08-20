"""Implementation of a singly linked list"""

class Node:
    """Node of a singly linked list"""
    def __init__(self, value: any):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """Singly linked list class"""
    def __init__(self):
        self.length: int = 0
        self.head: Node = None
        self.tail: Node = None
    
    def push(self, value: any) -> bool:
        """Adds an element at the end of a list"""
        new_node: Node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
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
    
    def shift(self) -> Node:
        """Removes the first node of a linked list"""
        if not self.head or self.length == 0:
            return None
        old_head: Node = self.head
        self.head: Node = old_head.next
        old_head.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return old_head
    
    def unshift(self, value: any) -> bool:
        """Adds a new node at the beginning of the list"""
        new_node: Node = Node(value)
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
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
    
    def set(self, index: int, value: any) -> bool:
        """Changes the value of a specific node in a list"""
        node: Node = self.get(index)
        if not node:
            return False
        node.value = value
        return True
    
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

    def traverse(self) -> None:
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

sll: SinglyLinkedList = SinglyLinkedList()
sll.push(23)
sll.push(24)
sll.push(25)
sll.push(22)
sll.push(18)
sll.push(45)
sll.push(33)

# sll.pop()
# sll.pop()

# sll.shift()

# sll.unshift(15)
# sll.unshift(10)

sll.set(sll.length-1, 234)


node: Node = sll.get(7)
try:
    print(f"Node is {node.value}")
except(AttributeError):
    print("Invalid index")

# sll.insert(0, 88)
# sll.insert(10, 567)
# sll.insert(2, 456)

# sll.remove(0)
# sll.remove(5)

sll.traverse()

try:
    print("===LIST INFORMATION===")
    print(f"Length of the list: {sll.length}")
    print(f"Head node: {sll.head.value}")
    print(f"Tail node: {sll.tail.value}")
except(AttributeError):
    print("The list is empty")
