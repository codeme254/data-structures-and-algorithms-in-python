"""Implementation of a queue data structure"""

class Node:
    """node of a queue"""
    def __init__(self, value: any):
        self.value = value
        self.next = None

class Queue:
    """Queue data structure"""
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.size: int = 0
    
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

    def print_queue(self):
        """Prints the queue"""
        if self.size == 0 or not self.first:
            return None
        current_node: Node = self.first
        while current_node != None:
            print(current_node.value, end=" ")
            current_node = current_node.next


q: Queue = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.dequeue()

q.print_queue()