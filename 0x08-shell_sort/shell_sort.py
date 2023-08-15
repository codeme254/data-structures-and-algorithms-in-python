"""Shell sort algorithm"""
from typing import List
from math import floor
def swap_list_elements(list: List[any], index1: int, index2: int):
    """
    Swaps two elements of a list in place
    """
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def shell_sort(list: List[any]):
    """
    Performs the shell sort algorithm on a list of elements of any data type
    """
    if len(list) <= 1:
        return list
    
    gap = floor(len(list) / 2)
    while gap > 0:
        i = 0
        j = gap
        while j < len(list):
            if list[i] > list[j]:
                swap_list_elements(list, i, j)
                temp_right = i
                temp_left = i - gap
                while temp_left >= 0:
                    if list[temp_right] < list[temp_left]:
                        swap_list_elements(list, temp_left, temp_right)
                        temp_right = temp_left
                        temp_left = temp_left - gap
                    else:
                        break
            i += 1
            j += 1
        gap = floor(gap/2)
    return list

print(shell_sort([23, 29, 15, 19, 31, 7, 9, 5, 2]))