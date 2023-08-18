"""Implementation of the merge sort algorithm"""
from typing import List
from math import floor
def merge(list1: List[any], list2: List[any]):
    """Merges two sorted lists together into one larger sorted list"""
    i: int = 0
    j: int = 0
    final_list: List[any] = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            final_list.append(list1[i])
            i += 1
        else:
            final_list.append(list2[j])
            j += 1
    while i < len(list1):
        final_list.append(list1[i])
        i += 1
    while j < len(list2):
        final_list.append(list2[j])
        j += 1
    return final_list

def merge_sort(list: List[any]):
    """Sorts a list of elements using merge sort"""
    if len(list) <= 1:
        return list
    mid: int = floor(len(list) / 2)
    left: List[any] = merge_sort(list[0:mid])
    right: List[any] = merge_sort(list[mid:len(list)])
    return merge(left, right)
