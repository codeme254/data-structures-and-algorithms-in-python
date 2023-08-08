## Linear search
Given a list, the simplest way to search for an element is to look at every element in the list and check if it's the value we want - **Linear Search**

### Linear search pseudocode
1. The functions accepts a list and a value.
1. Loop through the list and in each iteration, check whether the current element in the list is equal the value.
1. If it is, return the index at which the element was found.
1. If the value is never found, return -1.

```py
def linear_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return -1

print(linear_search([10, 1, 13, 4, 6], 13))
print(linear_search([10, 1, 13, 4, 6], 23))
```

Recursive linear search solution
```py
def linear_search(list, value, i):
    if i >= len(list):
        return -1
    if list[i] == value:
        return i
    i += 1
    return linear_search(list, value, i)

print(linear_search([10, 1, 13, 4, 6], 13, 0))
print(linear_search([10, 1, 13, 4, 6], 23, 0))
```

### Big O of linear search
O(1) - best case, the element is actually at index 0
O(n) - worst case
O(n) - Average case (we only care about the **general trend**)

## Binary Search
It is a much faster form of search.

Rather than eliminating one element at a time, you can eliminate half of the remaining elements at a time.

_**Binary search only works on sorted arrays**_

**This is a divide and conquer algorithm**

### Binary search pseudocode (assuming the list is sorted in ascending order)
1. Write a function that accepts a sorted list and a value.
1. Create a left pointer to the start of the array and a right pointer to the end of the list.
1. While the left pointer comes before the right pointer:
    1. Create a pointer in the middle - (left + right) / 2
    1. If the middle pointer points at the wanted value, return that index.
    1. If the value is too small, move the left pointer to where the middle pointer was.
    1. If the value is too large, move the right pointer to where the middle pointer was.

Implementation of binary search
```py
from math import ceil
def binary_search(list, value):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = ceil((left + right)/2)
        if (middle == left or middle == right) and list[middle] != value:
            return -1
        if list[middle] == value:
            return middle
        elif list[middle] > value:
            right = middle
        elif list[middle] < value:
            left = middle
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 20))
print(binary_search([1, 2, 3, 4], 2.3))
print(binary_search([1, 2, 3, 4], 1.3))
```

Alternative implementation of binary search
```py
from math import floor
def binary_search(list, value):
    start = 0
    end = len(list) - 1
    middle = floor((start + end) / 2)

    while (list[middle] != value and start <= end):
        if value < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = floor((start + end) / 2)

    if list[middle] == value:
        return middle
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 20))
print(binary_search([1, 2, 3, 4], 2.3))
print(binary_search([1, 2, 3, 4], 1.3))
```

Recursive implementation of binary search
```py
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
```

### Big O of binary search
Best case - O(1)

worst and average case - O(log n)

## Naive string search
Suppose you want to count the number of times a smaller string appears in a larger string.

### Naive string search pseudocode
1. Loop over a longer string
1. Loop over the shorter string (in an inner loop)
1. If the characters don't match, break out of the inner loop
1. If the characters do match, keep going.
1. If you complete the inner loop and find a match, increment the count of matches.
1. Return the count

Implementation 1
```py
def naive_string_count(long, short):
    count = 0
    for i in range(0, len(long)):
        for j in range(0, len(short)):
            if i + j >= len(long):
                return count
            if short[j] != long[i + j]:
                break
            if j == len(short) - 1:
                count += 1
    return count

print(naive_string_count("wow, you came, just wow", "wow"))
```

alternative implementation
```py
def count_string_appearance(parent_string, string):
    if len(string) > len(parent_string):
        return 0
    if len(string) == len(parent_string) and string != parent_string:
        return 0
    if len(string) == len(parent_string) and string == parent_string:
        return 1
    count = 0
    i = 0
    while i < len(parent_string):
        j = 0
        for j in range(0, len(string)):
            matching = True
            if i >= len(parent_string):
                return count
            if string[j] == parent_string[i]:
                i += 1
                continue
            elif string[j] != parent_string[i]:
                i += 1
                matching = False
                break
        if matching:
            count += 1
    return count

print(count_string_appearance("wow, you are here, just wow, wow, wow", "wow"))
print(count_string_appearance("wow, you are here, just wow, wow, wow", "w"))
```