"""implementation of quick sort algorithm"""

from typing import List
def swap_list_elements(list: List[any], index1: int, index2: int):
    """Swaps the positions of two elements in a list"""
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def pivot(list: List[any], start: int, end: int):
    """Returns the index of the pivot in a list"""
    if len(list) <= 0:
        return None
    current_pivot_index: int = start
    pivot_index: int = current_pivot_index
    i: int = start + 1
    while (i <= end):
        if list[current_pivot_index] > list[i]:
            pivot_index += 1
            swap_list_elements(list, pivot_index, i)
        i += 1
    swap_list_elements(list, current_pivot_index, pivot_index)
    print(list)
    return pivot_index

def quick_sort(list: List[any], left: int, right: int):
    """implements the quick sort algorithm on a list"""
    if left < right:
        pivot_idx: int = pivot(list, left, right)
        # left
        quick_sort(list, left, pivot_idx - 1)
        # right
        quick_sort(list, pivot_idx + 1, right)
    return list
