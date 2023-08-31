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
        index: int = len(self.values) - 1
        parentIndex: int = floor((index-1)/2)
        while self.values[parentIndex] < self.values[index]:
            swap_list_values(self.values, index, parentIndex)
            index = parentIndex
            parentIndex: int = floor((index-1)/2)
            if parentIndex < 0:
                break
        return self.values
    
    def extract_max(self):
        """Remove the maximum value of the max heap"""
        swap_list_values(self.values, 0, len(self.values) - 1)
        old_root: any = self.values.pop(len(self.values) - 1)
        self.sink_down()
        return old_root
        
    def sink_down(self):
        """sinks down and element to the right position in the heap after extracting max"""
        index: int = 0
        element: any = self.values[0]
        while True:
            left_child_index: int = (2 * index) + 1
            right_child_index: int = (2 * index) + 2
            left_child: any = None
            right_child: any = None
            swap: int = None
            if left_child_index < len(self.values):
                left_child = self.values[left_child_index]
                if left_child > element:
                    swap = left_child_index
            if right_child_index < len(self.values):
                right_child = self.values[right_child_index]
                if (swap == None and right_child > element) or (swap and right_child > left_child):
                    swap = right_child_index
            if swap == None:
                break
            swap_list_values(self.values, index, swap)
            index = swap
    
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
max_heap.insert(60)
max_heap.insert(22)

print(max_heap.extract_max())
max_heap.show_heap()