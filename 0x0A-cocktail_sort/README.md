# Cocktail shaker Sort
- Cocktail sort algorithm is meant to be an improvement of the bubble sort algorithm.
- It works on both directions, I.E it bubbles bigger values to the end of the list and once at the end of the list, it bubbles smaller values to the start of the list, this looks like a shaking manner and thus cocktail shaker algorithm.
- ```ALSO REFERRED TO AS BIDIRECTIONAL BUBBLE SORT ALGORITHM```

## Understand it better using the walkthrough below
- Suppose we are given the list [3, 1, 2, 5, 4, 0], let's sort it in ascending order using the cocktail shaker algorithm.
1. Start at the beginning of the list, use a variable i initialized to 0 to track this, compare it with element at i + 1, if it is greater swap them and if not ignore the swap, in this case, 3 is greater than 1 so we swap
    - [3, 1, 2, 5, 4, 0] changes to [```1, 3``` , 2, 5, 4, 0]
1. We increment i to 1 and compare element at i with element at i + 1, comparing 3 and 2, 3 is greater than 2 so we do a swap
    - [1, 3 , 2, 5, 4, 0] changes to [1, ```2, 3```, 5, 4, 0]
1. Same thing, increment i to 2 and compare the element at i with the element  at i + 1, in this case, 3 is less than 5 so no swapping is done.
1. Increment i to 3 and compare the element at i with the element at i + 1, in this case, 5 is greater than 4 so we do a swap.
    - [1, ```2, 3```, 5, 4, 0] changes to [1, 2 , 3, ```4, 5```, 0]
1. Increment i to 4 and compare the element at i with the element at i + 1, in this case, 5 is greater than 0 and this we do a swap.
    - [1, 2 , 3, 4, 5, 0] changes to [1, 2 , 3, 4, ```0, 5```]
1. Increasing i makes it to reach the end of the list, it's now time to start moving in the reverse direction.
1. Compare the value at i with the value at i - 1, if the value at i is greater than the value at i - 1, we don't do a swap, if it is less then we do a swap, remember we are now moving in the reverse direction.
1. In this case, 5 is greater than 0 so no swap is needed.
1. we decrement the value of i to 4 and compare the element at i with the element at i - 1, in this case, 0 is less than 4 so we do a swap.
    - [1, 2 , 3, 4, 0, 5] changes to [1, 2 , 3, ```0, 4```, 5]
1. we decrement the value of i to 3 and compare the element at i with the element at i - 1, in this case 0 is less than 3 so we do a swap.
    - [1, 2 , 3, 0, 4, 5] changes to [1, 2 , ```0, 3```, 4, 5]
1. Decrement the value of i to 2 and compare the value at i with the value at i - 1, in this case, 0 is less than 2 so we do a swap
    - [1, 2 , 0, 3, 4, 5] changes to [1, ```0, 2```, 3, 4, 5]
1. Decrement the value of i to 1 and compare the element at i with the element at i - 1, in this case, 0 is less than 1 so we do a swap.
    - [1, 0, 2, 3, 4, 5] changes to [```0, 1```, 2, 3, 4, 5]
1. Decrement i to 0 and now there is no element at i - 1.
1. At this point my list is sorted but in other lists, the list will not yet be sorted maybe, this pops the question ```HOW DO WE KNOW WHEN TO STOP IN COCKTAIL SORT```.
1. You guessed it right: ```WE STOP WHEN NO SWAP HAS BEEN MADE IN ANY PASS, COME TO THINK OF IT, IF A LIST IS SORTED AT ANY GIVEN PASS, NO SWAP WILL BE MADE AND IF THAT IS SO, IT MEANS THE LIST IS SORTED AND THAT IS THE END OF THE ALGORITHM```
1. This means that you can make as many passes as possible but if at any pass you don't do a swap, it means the list is finally sorted, in your code, you can use a variable to check this and use it to end the algorithm when your list is sorted.

Here goes the code implementation:

```python
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
```

And here are the test cases in case you want to check whether your implementation is correct:
```python
import unittest
from cocktail_sort import cocktail_sort

class TestCocktailSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        cocktail_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        cocktail_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        cocktail_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        cocktail_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        cocktail_sort(arr)
        self.assertEqual(arr, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        cocktail_sort(arr)
        self.assertEqual(arr, [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        cocktail_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        cocktail_sort(list)
        self.assertEqual(list, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        cocktail_sort(list)
        self.assertEqual(list, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        cocktail_sort(list)
        self.assertEqual(list, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        cocktail_sort(list)
        self.assertEqual(list, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        cocktail_sort(list)
        self.assertEqual(list, [23, 31, 44, 57, 69, 77, 83, 95])
    
    def test_random_list_with_negative_values(self):
        list = [44, 77, 69, 31, 23, 57, -95, -83]
        cocktail_sort(list)
        self.assertEqual(list, [-95, -83, 23, 31, 44, 57, 69, 77])
    
    def test_random_list_with_negative_values_2(self):
        list = [-5, -4, -1, -2, 0, -4]
        cocktail_sort(list)
        self.assertEqual(list, [-5, -4, -4, -2, -1, 0])
    
    def test_random_list_of_string_1(self):
        list = ['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']
        cocktail_sort(list)
        self.assertEqual(list, ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'orange', 'pear', 'watermelon'])
    
    def test_random_list_of_strings_2(self):
        list = ['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']
        cocktail_sort(list)
        self.assertEqual(list, ['orange', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon'])
    
    def test_random_list_of_strings_3(self):
        list = ['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']
        cocktail_sort(list)
        self.assertEqual(list, ['apricot', 'blueberry', 'cranberry', 'dragonfruit', 'fig', 'grapefruit'])
    
    def test_random_list_of_strings_4(self):
        list = ['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']
        cocktail_sort(list)
        self.assertEqual(list, ['banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi'])

if __name__ == '__main__':
    unittest.main()
```