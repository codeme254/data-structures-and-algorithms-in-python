"""Implementation of a doubly linked list"""

class Node:
    """Node of a doubly linked list"""
    def __init__(self, value: any):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    """Doubly linked list"""
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0
    
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
    
    def set(self, index: int, value: any):
        """Replaces the value of a node in a doubly linked list"""
        node: Node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
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
    
    def print_list(self):
        """Prints the list"""
        try:
            print(f"Length of list: {self.length}")
            print(f"Head node value: {self.head.value}")
            print(f"Tail node value: {self.tail.value}")
        except AttributeError:
            print("List is Empty!")
            return None

        current: Node = self.head
        print(f"{current.value} -> ", end=" ")

        while current != None:
            current = current.next
            try:
                print(f"{current.value} ->", end=" ")
            except AttributeError:
                print("None")

        # printing in reverse
        current: Node = self.tail
        print(f"{current.value} -> ", end=" ")

        while current != None:
            current = current.previous
            try:
                print(f"{current.value} -> ", end=" ")
            except AttributeError:
                print("None")

dll: DoublyLinkedList = DoublyLinkedList()

dll.push(20)
dll.push(25)
dll.push(30)
dll.push(45)
dll.push(55)
dll.push(23)
dll.push(90)

dll.pop()

dll.shift()

dll.unshift(2)

print(dll.get(5).value)

dll.set(0, 1.1)

print(dll.insert(0, 1.0))
print(dll.insert(7, 100))
print(dll.insert(4, 40))

dll.remove(0)
dll.remove(3)
dll.remove(6)
dll.print_list()
