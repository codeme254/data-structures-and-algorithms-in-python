# base cases - start > end - element not found, return -1
# list[middle] == value
from math import ceil
def binary_search(list, value, start, end):
    middle = ceil((start + end) / 2)
    if middle == start or middle == end and list[middle] != value:
        return -1
    if list[middle] == value:
        return middle
    if list[middle] > value:
        end = middle
        if start > end:
            return -1
        if start == end and list[start] != value and list[end] != value:
            return -1
        return binary_search(list, value, start, end)
    if list[middle] < value:
        start = middle
        if start > end:
            return -1
        if start == end and list[start] != value and list[end] != value:
            return -1
        return binary_search(list, value, start, end)

print(binary_search(list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], value=8,  start= 0, end= 11))
print(binary_search(list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], value=11, start=  0,end=  11))
print(binary_search(list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], value=21, start=  0,end=  11))
print(binary_search(list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], value=2.1, start=  0,end=  11))