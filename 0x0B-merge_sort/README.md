## Merging list
- In order to implement merge sort, it is useful to first implement a function responsible for merging two lists.
1. Given two lists which are sorted, this helper function should create a new list which is also sorted, and consists of all the elements in the two input lists.
1. The function should run in O(n + m) time and space and should not modify the parameters passed into it.
1. Assuming our two lists are [1, 4, 5] and [2, 3, 9, 12]
1. Have a variable eg i initialized with 0 to iterate the first list and j initialized with 0 to iterate the second list.
1. If list1[i] is less than list2[j], append list1[i] to the merged list, if not (i.e list2[i] is the lesser one), then append list2[j] to the sorted list. Increment the counter whose list element was appended eg if list1's element was appended increment i, if it was list 2, increment j
    - in this case, 1 is less than 2 so we append 1 and increment i. Sorted array is [1]
1. Repeat the step above until you reach either ends, i.e if i reaches the length of its list first, we stop the step above, if j, we do the same.
1. Once we finish one list, we push the elements of the other list in.

Here is the implementation of merging:
```python
"""Implementation of the merge sort algorithm"""
from typing import List
def merge(list1: List[any], list2: List[any]):
    """Merges two sorted lists together into one larger sorted list"""
    i = 0
    j = 0
    final_list = []
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
```

and here are the tests
```python
import unittest
from merge_sort import merge

class TestMerge(unittest.TestCase):
    """Tests the merge method"""
    def test_both_lists_empty(self):
        """Tests the condition where both lists are empty"""
        list1 = []
        list2 = []
        result = merge(list1, list2)
        self.assertEqual(result, [])
    
    def test_list_1_empty(self):
        """Tests the case where only list 1 is empty"""
        list1 = []
        list2 = [2, 8, 10]
        result = merge(list1, list2)
        self.assertEqual(result, [2, 8, 10])
    
    def test_list_2_empty(self):
        """Tests the condition where only list 2 is empty"""
        list1 = [2, 8, 10]
        list2 = []
        result = merge(list1, list2)
        self.assertEqual(result, [2, 8, 10])
    
    def test_both_lists_with_equal_number_of_elements(self):
        """Tests the condition where both lists have equal length"""
        list1 = [1, 5, 12]
        list2 = [2, 4, 9]
        result = merge(list1, list2)
        self.assertEqual(result, [1, 2, 4, 5, 9, 12])
    
    def test_list_1_with_more_elements(self):
        """Tests the condition where list one has more elements than list 2"""
        list1 = [1, 5, 8, 12, 14]
        list2 = [2, 4, 9]
        result = merge(list1, list2)
        self.assertEqual(result, [1, 2, 4, 5, 8, 9, 12, 14])
    
    def test_list_2_with_more_elements(self):
        """Tests the condition where list two has more elements than list 1"""
        list1 = [1, 5, 8]
        list2 = [2, 4, 9, 12, 14]
        result = merge(list1, list2)
        self.assertEqual(result, [1, 2, 4, 5, 8, 9, 12, 14])

if __name__ == "__main__":
    unittest.main()
```

## The merge sort algorithm
1. Break up the given list into halves until yoy have list that are empty or have one element.
1. Once you have smaller sorted list, merge those lists with other sorted lists until you are back at the full length of the list.
1. Once the list has been merged back together, return the merged (and sorted) list.

Here goes the full implementation of merge sort
```python
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
```

And here are the unit tests in case you want to run them
```py
import unittest
from merge_sort import merge_sort

class TestCountingSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        result = merge_sort(arr)
        self.assertEqual(result, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        result = merge_sort(arr)
        self.assertEqual(result, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        result = merge_sort(arr)
        self.assertEqual(result, [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        result = merge_sort(list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        result = merge_sort(list)
        self.assertEqual(result, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        result = merge_sort(list)
        self.assertEqual(result, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        result = merge_sort(list)
        self.assertEqual(result, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        result = merge_sort(list)
        self.assertEqual(result, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        result = merge_sort(list)
        self.assertEqual(result, [23, 31, 44, 57, 69, 77, 83, 95])
    
    def test_random_list_with_negative_values(self):
        list = [44, 77, 69, 31, 23, 57, -95, -83]
        result = merge_sort(list)
        self.assertEqual(result, [-95, -83, 23, 31, 44, 57, 69, 77])
    
    def test_random_list_with_negative_values_2(self):
        list = [-5, -4, -1, -2, 0, -4]
        result = merge_sort(list)
        self.assertEqual(result, [-5, -4, -4, -2, -1, 0])
    
    def test_random_list_of_string_1(self):
        list = ['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']
        result = merge_sort(list)
        self.assertEqual(result, ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'orange', 'pear', 'watermelon'])
    
    def test_random_list_of_strings_2(self):
        list = ['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']
        result = merge_sort(list)
        self.assertEqual(result, ['orange', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon'])
    
    def test_random_list_of_strings_3(self):
        list = ['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']
        result = merge_sort(list)
        self.assertEqual(result, ['apricot', 'blueberry', 'cranberry', 'dragonfruit', 'fig', 'grapefruit'])
    
    def test_random_list_of_strings_4(self):
        list = ['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']
        result = merge_sort(list)
        self.assertEqual(result, ['banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi'])

if __name__ == '__main__':
    unittest.main()
```

## Big O of merge sort
On the best, average and worst time complexities - O(n log n)
Space complexity of O(n)