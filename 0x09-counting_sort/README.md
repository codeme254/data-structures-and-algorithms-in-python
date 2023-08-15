# Counting Sort
- It is one of the most unique sorting algorithms in that it doesn't do any comparison.
- This sorting algorithm works with positive integer values only.
- This means that for counting sort, [10, 12, 3, 13, 9, 6] - will be sorted fine
- [-10, 12, 3, 13, 9, 6] wont work because for counting sort all the elements should be positive integer numbers.
- ["Jesse", "Krugger"] - won't work because again, counting sort will only work when all elements are positive integer values, not strings, floats, negative integers nor anything else.

- The idea behind counting sort is that we create a new list containing the frequencies of elements from the original list and then use this frequencies to sort the original list in order without doing any comparisons.

## Understand it better using the walkthrough below.
1. Given this list, we want to use counting sort algorithm to sort it in ascending order: [1, 4, 1, 2, 7, 5, 2].
1. First find the biggest integer in the list, this will be used to create a frequency list of that range+1, in this case, the largest value is 7 which means our frequency list will have a length of 8, we will discuss later why this is so.
1. Create a list of the length range+1 and initialize each element to be 0. ```[0, 0, 0, 0, 0, 0, 0, 0]```.
1. For each element in the original list, increment the value in the frequency list at the corresponding index as shown below:
    - For 1, we will increment the frequency list at index 1 with 1, the list will be updated to -> ```[0, 1, 0, 0, 0, 0, 0, 0]```
    - For 4, we will increment the frequency list at index 4 with 1, the list will be updated to -> ```[0, 1, 0, 0, 1, 0, 0, 0]```
    - For the next element 1, we  will increment the frequency at index 1 with 1, the list will be updated to -> ```[0, 2, 0, 0, 1, 0, 0, 0]```
    - For the next element 2, we will increment the frequency at index 2 with 1, the list will be updated to -> ```[0, 2, 1, 0, 1, 0, 0, 0]```
    - For the next element 7 (which we saw was our largest value and gave us the range), we will increment the frequency at index 7 with 1, the list will be updated to -> ```[0, 2, 1, 0, 1, 0, 0, 1]``` - ```THIS EXPLAINS WHY THE LENGTH OF OUR FREQUENCY LIST HAD TO BE RANGE+1 AND THAT IS BECAUSE DUE TO ZERO INDEXING NATURE OF LISTS, THE LARGEST VALUE WILL HAVE TO FIT AT ITS SIZE PLUS 1```
    - For the next element 5, we will increment the frequency list at index 5 with 1, the list will be updated to -> ```[0, 2, 1, 0, 1, 1, 0, 1]```
    - For the last element 2, we will increment the frequency list at index 2 with 1, the list will be updated to -> ```[0, 2, 2, 0, 1, 1, 0, 1]```
1. Now we have our frequency list ```[0, 2, 2, 0, 1, 1, 0, 1]``` which we will use to create our sorted list.
1. Use the frequency list to sort the list, you can create a new list or do it in place, for this walkthrough, we will do it in place, so create a new list.
1. Loop the frequency list and in each pass, if the value is zero, you don't do anything, if the value is any number larger than zero, append the current iteration value to the sorted list as many times as the current value is, eg at index 1, we have 2, so we append two 1s, at index 2, we have 2, so we append 2 2s to the sorted list, at index 3, we have a zero so we don't do anything, at index 4, we have 1 so we append one 4 into the sorted list and so on and so forth.

```python
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
```

Here are some test cases you can run to check if your implementation worked
```python
import unittest
from counting_sort import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        result = counting_sort(arr)
        self.assertEqual(result, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        result = counting_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        result = counting_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = counting_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        result = counting_sort(arr)
        self.assertEqual(result, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        result = counting_sort(arr)
        self.assertEqual(result, [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        result = counting_sort(list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        result = counting_sort(list)
        self.assertEqual(result, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        result = counting_sort(list)
        self.assertEqual(result, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        result = counting_sort(list)
        self.assertEqual(result, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        result = counting_sort(list)
        self.assertEqual(result, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        result = counting_sort(list)
        self.assertEqual(result, [23, 31, 44, 57, 69, 77, 83, 95])
    
    def test_random_list_with_negative_values(self):
        list = [44, 77, 69, 31, 23, 57, -95, -83]
        result = counting_sort(list)
        self.assertEqual(result, None)
    
    def test_random_list_with_negative_values_2(self):
        list = [-5, -4, -1, -2, 0, -4]
        result = counting_sort(list)
        self.assertEqual(result, None)
    
    def test_random_list_of_string_1(self):
        list = ['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']
        result = counting_sort(list)
        self.assertEqual(result, None)
    
    def test_random_list_of_strings_2(self):
        list = ['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']
        result = counting_sort(list)
        self.assertEqual(result, None)
    
    def test_random_list_of_strings_3(self):
        list = ['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']
        result = counting_sort(list)
        self.assertEqual(result, None)
    
    def test_random_list_of_strings_4(self):
        list = ['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']
        result = counting_sort(list)
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
```