"""implementation of a stack"""
class Node:
    """Node of a stack"""
    def __init__(self, value: any):
        self.value = value
        self.next = None


class Stack:
    """Stack data structure"""
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.size: int = 0
    
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
    
    def print_stack(self):
        """prints the stack"""
        if self.size == 0 or not self.first:
            return None
        current_node: Node = self.first
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

stack: Stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.pop()
stack.print_stack()