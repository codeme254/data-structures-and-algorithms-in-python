"""implementation of the cocktail sort algorithm"""
from typing import List
def swap_list_elements(list: List[any], index1: int, index2: int):
    """swaps 2 elements of a list in place"""
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def cocktail_sort(list: List[any]):
    """Sorts a list of elements in ascending order using the cocktail sort algorithm"""
    if len(list) <= 1:
        return list
    
    keep_working = True
    i = 0
    while keep_working:
        swap_happened = False
        while i < len(list) - 1:
            if list[i] > list[i+1]:
                swap_list_elements(list, i, i+1)
                swap_happened = True
            i += 1
        i = len(list) - 1
        while i > 0:
            if list[i] < list[i-1]:
                swap_list_elements(list, i, i-1)
                swap_happened = True
            i -= 1
        
        if swap_happened == False:
            return list

print(cocktail_sort([3, 1, 4, 9, 2, 1, 0]))
