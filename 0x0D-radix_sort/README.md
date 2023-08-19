# Radix sort
It is a special sorting algorithm that works on a list of numbers.

It never makes comparison between elements.

It exploits the fact that information about the size of a number is encoded in the number of digits.

More digits mean bigger number.

It can only work on positive integer numbers.

## Helper functions with radix sort
In order to implement radix sort, it is helpful to build a few helper functions first:
- get_digit(num, place) - returns the digit in a number at the given place from the end, i.e getDigit(12345, 0); returns 5
- digit_count(number) - returns the length of a positive integer number.
- most_digits(numbers) - takes a list of integers and returns the length of the largest integer.

Here are the above implementations

Get digit
```python
def get_digit(number: int, place: int):
    """Returns digit from the number at a given place"""
    # get_digit(12345, 0) returns 5
    number_str = str(number)
    if place >= number_str:
        return 0
    reversed_str: str = ""
    i: int = len(number_str) - 1
    while i >= 0:
        reversed_str += number_str[i]
        i -= 1
    return reversed_str[place]
```

Digit count
```python
def digit_count(number: int):
    """Returns the length of an integer number"""
    return len(str(number))
```

Most digits
```python
def most_digits(numbers: List[int]):
    """Returns the number of digits in the largest numbers in the list"""
    most_numbers_length = 0
    for number in numbers:
        current_count = digit_count(number)
        if current_count > most_numbers_length:
            most_numbers_length = current_count
    return most_numbers_length
```

## Radix sort pseudocode
- Define a function that accepts a list of numbers.
- Figure out how many digits the largest number has.
- loop from 0 up to this largest number of digits.
- For each iteration of the loop:
    - Create buckets for each digit 0-9
    - Place each number in the corresponding bucket based on its current digit.
- Replace the existing list with values in the buckets starting with 0 and going up to 9
- Return list at the end.

Here is the full implementation of radix sort

```python
"""Implementation of the radix sort algorithm"""

from typing import List
def get_digit(number: int, place: int):
    """Returns digit from the number at a given place"""
    # get_digit(12345, 0) returns 5
    number_str = str(number)
    if place >= len(number_str):
        return 0
    reversed_str: str = ""
    i: int = len(number_str) - 1
    while i >= 0:
        reversed_str += number_str[i]
        i -= 1
    return reversed_str[place]
    
def digit_count(number: int):
    """Returns the length of an integer number"""
    return len(str(number))

def most_digits(numbers: List[int]):
    """Returns the number of digits in the largest numbers in the list"""
    most_numbers_length = 0
    for number in numbers:
        current_count = digit_count(number)
        if current_count > most_numbers_length:
            most_numbers_length = current_count
    return most_numbers_length

def radix_sort(lst: List[int]):
    """Sorts a list of positive integer values using the radix sort algorithm"""
    largest_range = most_digits(lst)
    for i in range(0, largest_range):
        buckets = [[] for i in range(0, 10)]
        for number in lst:
            current_digit = int(get_digit(number, i)) ## 3221 - 1
            buckets[current_digit].append(number)
        lst = [element for sublist in buckets for element in sublist]
    return lst
```

And here are some test cases for radix sort in case you want to test yours

```python
import unittest
from radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        result = radix_sort(arr)
        self.assertEqual(result, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        result = radix_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        result = radix_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = radix_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        result = radix_sort(arr)
        self.assertEqual(result, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        result = radix_sort(arr)
        self.assertEqual(result , [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        result = radix_sort(list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        result = radix_sort(list)
        self.assertEqual(result, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        result = radix_sort(list)
        self.assertEqual(result, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        result = radix_sort(list)
        self.assertEqual(result, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        result = radix_sort(list)
        self.assertEqual(result, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        result = radix_sort(list)
        self.assertEqual(result, [23, 31, 44, 57, 69, 77, 83, 95])

if __name__ == '__main__':
    unittest.main()
```

## Big O of radix sort
For the best, worst and average time complexity - O(nk)

where n is the length of the array and k is the length of the largest integer

Runs in a space complexity of O(n + k)
