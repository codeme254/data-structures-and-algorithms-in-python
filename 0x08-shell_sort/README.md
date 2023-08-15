# Shell sort
- It is like insertion sort but with the goal of reducing the number of swaps happening as much as possible.
- Instead of swapping and comparing adjacent elements in every pass, it works around the concept of a ```gap```.
- It's designed to improve the performance of Insertion Sort by sorting elements that are far apart before eventually sorting them in close proximity. 

## Understand better with the example walkthrough below (sorting in ascending order).
- assuming we have this list -> [23, 29, 15, 19, 31, 7, 9, 5, 2]

1. We start by creating a gap, there are many methods of choosing a gap, in this case we take the floor value of the length of the list above divided by 2 -> 9/2 = 4.5 = 4
1. This means we will compare the element at index 0 with the element at index 4.
1. Compare the element at index 0 (index i) with the element at index 4 (index j) (the gap), i.e 23 and 31, 23 is less than 31 so no swapping will be done since we are sorting in ascending order.
1. Increment i with 1 and j with 1 which means we are now comparing element at index 1 with element at index 5, which is 29 and 7, 29 is greater than 7 so we do a swap.
    - [23, 29, 15, 19, 31, 7, 9, 5, 2] changes to [23, ```7```, 15, 19, 31, ```29```, 9, 5, 2]
1. Increment i with 1 and j with 1 which means we are now checking 15 and 9, 15 is greater than 9 which means we do a swap.
    - [23, 7, 15, 19, 31, 29, 9, 5, 2] changes to [23, 7, ```9```, 19, 31, 29, ```15```, 5, 2]
1. Increment i with 1 and j with 1 which means we are now comparing 19 with 5, 19 is greater than 5 so we do a swap
    - [23, 7, 9, 19, 31, 29, 15, 5, 2] changes to [23, 7, 9, ```5```, 31, 29, 15, ```19```, 2]
1. We increase i with 1 and j with 1 which means we are now comparing 31 and 2, 31 is greater than 2 which means we do a swap.
    - [23, 7, 9, 5, 31, 29, 15, 19, 2] changes to [23, 7, 9, 5, ```2```, 29, 15, 19, ```31```]
1. GOTCHA:: we are supposed to compare the element at index i with the element at index i - gap, write now, i is equal to 4 and gap is equal to 4 and 4 - 4 is equal to 0, there exists an element at index 0 thus we need to compare backwards and swap. We did not do that in the previous steps because i - 4 would have resulted in a number less than 0 which would lead to indexOutOfRange errors if we tried to do so but right now we are doing so because i - gap is a valid index value.
1. This means we will compare 2 with 23 which is at index i - gap. 23 is greater than 2, so we do a swap.
    - [23, 7, 9, 5, 2, 29, 15, 19, 31] changes to [```2```, 7, 9, 5, ```23```, 29, 15, 19, 31]
1. The first pass is over and it's now time for a second pass, this means we need to update the gap, there are many ways of updating a gap, in this case we will simply take the floor value of gap/2, i.e 4/2 which is 2.
1. We are now comparing elements with a gap of 2, which means i will start at 0 and j will start at 2. This means we are comparing 2 and 9, 2 is less than 9 so we don't do anything.
1. Increment i with 1 and j with 1 which means we are comparing 7 and 5, 7 is greater than 5 and this means a swap should be done as shown below.
    - [2, 7, 9, 5, 23, 29, 15, 19, 31] changes to [2, ```5```, 9, ```7```, 23, 29, 15, 19, 31]
    - From current position of i, there is no element at i - gap i.e i - 2. So no backward comparison or operation will be done.
1. Increment the value of i with 1 and the value of j with 1 which means we are comparing 9 and 23, 9 is greater than 23, so no swapping will be done.
1. Increment the value of i with 1 and the value of j with 1 which means we are now comparing 7 and 29, 7 is less than 29 so no swapping will be done.
1. Increment the value of i with 1 and the value of j with 1 which means we are now comparing 23 and 15, 23 is greater than 15 which means we need to do a swap.
    - [2, 5, 9, 7, 23, 29, 15, 19, 31] changes to [2, 5, 9, 7, ```15```, 29, ```23```, 19, 31].
    - Since we have done a swap, we check i - gap, i.e i - 2 which is element 9, comparing 9 and 15, 9 is less than 15 so no swapping is done.
1. Increment the value of i with i and j with 1, which means we are now comparing 29 and 19, 29 is greater than 19 which means we swap.
    - [2, 5, 9, 7, 15, 29, 23, 19, 31] changes to [2, 5, 9, 7, 15, ```19```, 23, ```29```, 31]
    - since we have done a swap, we check i - gap i.e i - 2 which is 7, 7 is less than 29 so there is no swapping.
1. Increment i with 1 and j with 1 which means we are comparing 23 and 31, 23 is less than 31 so no action is going to be taken.
1. We now go to the third pass, we update the gap - 2/2 which is 1, the current value of gap now is 1. ```At gap 1, shell sort works similar to insertion sort but with VERY MINIMAL SWAPS.```
1. i is at 0 and j at 1, which means we are comparing 2 and 5, 2 is less than 5 so no swap is done.
1. Increment i with 1 and j with 1 which means we are comparing 5 and 9, 5 is less than 9 so no swap is done.
1. Increment i with 1 and j with 1 which means we are now comparing 9 and 7, 9 is greater than 7 so we need to swap.
    - [2, 5, 9, 7, 15, 19, 23, 29, 31] changes to [2, 5, ```7```, ```9```, 15, 19, 23, 29, 31]
    - We have done a swap which means we compare element at i with element at i - gap, this means we are comparing 7 and 5 and they are in the correct order, so no swapping is done.
1. Increment i with 1 and j with 1 which means we are comparing 9 and 15 and they are in the correct order so no swapping is done.
1. Increment i with 1 and j with 1 which means we are comparing 15 and 19 and they are in the correct order and thus no swapping is done.
1. Increment i with 1 and j with 1 which means we are comparing 19 and 23 and they are in the correct order so no swapping is done.
1. Increment i with 1 and j with 1 which means we are comparing 23 and 23 and they are in the correct order so no swapping is done.
1. Increment i with 1 and j with 1 which means we are comparing 29 and 31 and they are in the correct order which means no swapping is done.
1. We have reached the end of the third pass with the gap being 1, any further attempt to update the gap will make it 0 or less and at this point, the algorithm is done and our list is sorted.

[2, 5, 7, 9, 15, 19, 23, 29, 31]

### NOTE: ALL SWAPPING IS DONE IN PLACE, DO NOT CREATE NEW LISTS.

Here is the implementation of the shell sort algorithm
```py
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
```

If you want to run some test cases here they go
```py
import unittest
from shell_sort import shell_sort

class TestMySort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        shell_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        shell_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        shell_sort(arr)
        self.assertEqual(arr, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        shell_sort(arr)
        self.assertEqual(arr, [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        shell_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        shell_sort(list)
        self.assertEqual(list, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        shell_sort(list)
        self.assertEqual(list, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        shell_sort(list)
        self.assertEqual(list, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        shell_sort(list)
        self.assertEqual(list, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        shell_sort(list)
        self.assertEqual(list, [23, 31, 44, 57, 69, 77, 83, 95])
    
    def test_random_list_of_string_1(self):
        list = ['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']
        shell_sort(list)
        self.assertEqual(list, ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'orange', 'pear', 'watermelon'])
    
    def test_random_list_of_strings_2(self):
        list = ['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']
        shell_sort(list)
        self.assertEqual(list, ['orange', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon'])
    
    def test_random_list_of_strings_3(self):
        list = ['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']
        shell_sort(list)
        self.assertEqual(list, ['apricot', 'blueberry', 'cranberry', 'dragonfruit', 'fig', 'grapefruit'])
    
    def test_random_list_of_strings_4(self):
        list = ['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']
        shell_sort(list)
        self.assertEqual(list, ['banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi'])

if __name__ == '__main__':
    unittest.main()

```