"""Counting sort algorithm"""

from typing import List
def counting_sort(list: List[int]):
    """
    sorts a list of positive integer numbers using the counting sort algorithm
    """
    if len(list) <= 1:
        return list
    largest_value = float('-inf')
    for i in range(0, len(list)):
        if not isinstance(list[i], int):
            return None
        if list[i] < 0:
            return None
        if list[i] > largest_value:
            largest_value = list[i]

    frequency_array = [0] * (largest_value + 1)
    for i in range(0, len(list)):
        frequency_array[list[i]] += 1
    sorted_list = []
    for i in range(0, len(frequency_array)):
        if frequency_array[i] == 0:
            continue
        else:
            for j in range(1, frequency_array[i]+1):
                sorted_list.append(i)
    return sorted_list
