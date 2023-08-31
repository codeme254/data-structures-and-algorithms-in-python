""""Binary heaps implementation"""

from typing import List
from math import floor

def swap_list_values(list: List, index1: int, index2: int):
    """swaps the elements of a list in place"""
    temp: any = list[index1]
    list[index1] = list[index2]
    list[index2] = temp


class MaxBinaryHeap:
    """max binary heap"""
    def __init__(self):
        self.values: List[any] = []
    
    def insert(self, value: any):
        """Inserts a value into the heap"""
        self.values.append(value)
        self.bubble_up()
    
    def bubble_up(self):
        """Puts a value in the correct space in the heap"""
        index: int = len(self.values) - 1
        element: any = self.values[index]
        while index > 0:
            parent_index: int = floor((index - 1)/2)
            parent: any = self.values[parent_index]
            if element <= parent:
                break
            swap_list_values(self.values, index, parent_index)
            index = parent_index
    
    def show_heap(self):
        """prints the values list"""
        print(self.values)
        for i in range(0, len(self.values)):
            try:
                print(f"{self.values[i]}", end=" ")
                print(f"Left: {self.values[(2 * i) + 1]}", end=" ")
                print(f"Right: {self.values[(2 * i) + 2]}")
            except IndexError:
                print(f"{self.values[i]} has either no either right or left child or both")

max_heap: MaxBinaryHeap = MaxBinaryHeap()
max_heap.insert(39)
max_heap.insert(41)
max_heap.insert(12)
max_heap.insert(27)
max_heap.insert(33)
max_heap.insert(18)
max_heap.insert(55)

max_heap.show_heap()