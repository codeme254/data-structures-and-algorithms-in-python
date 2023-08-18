# Quick sort
Like merge sort, it exploits the fact that arrays of 0 or 1 element are always sorted.

Works by selecting one element (called the ```pivot``` ) and finding the index where the pivot should end up in the sorted array.

All elements less than the pivot will move to the left and all the numbers greater than it will move to the right.

Once the pivot is positioned appropriately, quick sort can be applied on either side of the pivot.  

Example
---
If we have the list [5, 2, 1, 8, 4, 5, 6, 3]

We pick the first element(5) to be the pivot, the list would end up as  
[3, 2, 1, 4, 5, 7, 6, 8]

All elements greater than 5 (the pivot) have been taken to the right of it and all elements less than 5 have been taken to the left.

Repeating this to the left and the right of the current pivot will sort the list.

The process of finding the correct spot for the pivot is called partitioning.

## Pivot Helper
- In order to implement merge sort, it's useful to first implement a function responsible for arranging elements in an array on either sides of the pivot.
- Given an array, this helper function should designate an element as the pivot.
- it should then rearrange the array such that all elements less than the pivot are moved to the left and all those greater are moved to the right.
- The function should return the index of the pivot, not the element at that index.

## Pivot helper pseudocode
1. It should accept three arguments: a list, a start index and an end index, the start index can default to 0 and the end index can default to list length minus 1.
1. Grab the pivot from the start of the array.
1. Store the current pivot index in a variable (this will keep track of where the pivot should end up).
1. Loop through the list from the start to the end.
    1. If the pivot is greater then the current element, increment the pivot index variable and then swap the current element with the element at the pivot index.
1. At the end, swap the pivot with the element at the current pivot index.
1. Return the pivot index.

Here goes the implementation of this pivot function

```python
"""implementation of quick sort algorithm"""

from typing import List
def swap_list_elements(list: List[any], index1: int, index2: int):
    """Swaps the positions of two elements in a list"""
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def pivot(list: List[any], start: int = 0, end: int = len(list)-1):
    """Returns the index of the pivot in a list"""
    if len(list) <= 0:
        return None
    start = 0
    end = len(list) - 1
    current_pivot_index: int = 0
    pivot_index: int = current_pivot_index
    i: int = start
    while (i <= end):
        if list[current_pivot_index] > list[i]:
            pivot_index += 1
            swap_list_elements(list, pivot_index, i)
        i += 1
    swap_list_elements(list, current_pivot_index, pivot_index)
    print(list)
    return pivot_index
```

And here are the test cases just in case you want to test your own implementation

```python
import unittest
from quick_sort import pivot

class TestPivot(unittest.TestCase):
    def test_empty_list(self):
        list = []
        pivot_idx = pivot(list, 0, 0)
        self.assertIsNone(pivot_idx)
    
    def test_list_with_one_element(self):
        list = [2]
        pivot_idx = pivot(list, 0, 0)
        self.assertEqual(pivot_idx, 0)
    
    def test_list_with_positive_integer_elements(self):
        list = [3, 1, 9, 12, 2, 8, 14]
        pivot_idx = pivot(list, 0, len(list))
        self.assertEqual(pivot_idx, 2)
    
    def test_list_with_negative_integers(self):
        list = [-2, -8, -1, -9, -12]
        pivot_idx = pivot(list, 0, len(list))
        self.assertEqual(pivot_idx, 3)
    
    def test_with_floating_point_positive_value(self):
        list = [2.5, 2.8, 1.2, 3, 2.2]
        pivot_idx = pivot(list, 0, len(list))
        self.assertEqual(pivot_idx, 2)
    
    def test_with_negative_floating_point_values(self):
        list = [-2.5, -2.8, -1.2, -3, -2.2]
        pivot_idx = pivot(list, 0, len(list))
        self.assertEqual(pivot_idx, 2)
    
    def test_with_strings(self):
        list = ["Ball", "Art", "Alien", "Craft", "JigSaw"]
        pivot_idx = pivot(list, 0, len(list))
        self.assertEqual(pivot_idx, 2)

if __name__ == "__main__":
    unittest.main()
```

## Quick sort Pseudocode
1. Call the pivot helper on the list
1. Recursively call your quick sort function on the left of the pivot and on the right of the pivot (don't include the pivot).
1. Your base case occurs when either of the sub lists is less than 2 elements.

Here is the final implementation of the quick sort algorithm
```python
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
```

And here are the test cases just in case you want to test your implementation
```python
import unittest
from quick_sort import quick_sort

class TestMySort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, [23, 31, 44, 57, 69, 77, 83, 95])
    
    def test_random_list_of_string_1(self):
        list = ['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'orange', 'pear', 'watermelon'])
    
    def test_random_list_of_strings_2(self):
        list = ['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, ['orange', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon'])
    
    def test_random_list_of_strings_3(self):
        list = ['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, ['apricot', 'blueberry', 'cranberry', 'dragonfruit', 'fig', 'grapefruit'])
    
    def test_random_list_of_strings_4(self):
        list = ['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']
        quick_sort(list, 0, len(list)-1)
        self.assertEqual(list, ['banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi'])

if __name__ == '__main__':
    unittest.main()
```

## Big O of quick sort
- The best and average cases are O(n log n) and the worst case is O(n^2^)
- The worst case is because we are always using the first element as the pivot and this is dangerous if the list is or nearly sorted because we keep flipping too many elements.