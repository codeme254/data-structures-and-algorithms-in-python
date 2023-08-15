import unittest
from insertion_sort import insertion_sort

class TestMySort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_single_element_list(self):
        arr = [42]
        insertion_sort(arr)
        self.assertEqual(arr, [42])

    def test_duplicate_elements(self):
        arr = [5, 2, 8, 2, 5, 8, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [2, 2, 5, 5, 5, 8, 8])

    def test_random_list_2(self):
        list = [5, 4, 3, 2, 1]
        insertion_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])
    
    def test_random_list_3(self):
        list = [12, 7, 18, 5, 11, 9, 6, 2, 3, 14]
        insertion_sort(list)
        self.assertEqual(list, [2, 3, 5, 6, 7, 9, 11, 12, 14, 18])
    
    def test_random_list_4(self):
        list = [33, 25, 19, 29, 8, 36, 42, 17]
        insertion_sort(list)
        self.assertEqual(list, [8, 17, 19, 25, 29, 33, 36, 42])
    
    def test_random_list_5(self):
        list = [64, 73, 55, 91, 88, 60, 82, 47]
        insertion_sort(list)
        self.assertEqual(list, [47, 55, 60, 64, 73, 82, 88, 91])
    
    def test_random_list_6(self):
        list = [52, 15, 70, 39, 4, 63, 86, 28]
        insertion_sort(list)
        self.assertEqual(list, [4, 15, 28, 39, 52, 63, 70, 86])
    
    def test_random_list_7(self):
        list = [44, 77, 69, 31, 23, 57, 95, 83]
        insertion_sort(list)
        self.assertEqual(list, [23, 31, 44, 57, 69, 77, 83, 95])
    
    def test_random_list_of_string_1(self):
        list = ['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']
        insertion_sort(list)
        self.assertEqual(list, ['apple', 'banana', 'cherry', 'grape', 'kiwi', 'orange', 'pear', 'watermelon'])
    
    def test_random_list_of_strings_2(self):
        list = ['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']
        insertion_sort(list)
        self.assertEqual(list, ['orange', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon'])
    
    def test_random_list_of_strings_3(self):
        list = ['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']
        insertion_sort(list)
        self.assertEqual(list, ['apricot', 'blueberry', 'cranberry', 'dragonfruit', 'fig', 'grapefruit'])
    
    def test_random_list_of_strings_4(self):
        list = ['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']
        insertion_sort(list)
        self.assertEqual(list, ['banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew', 'kiwi'])

if __name__ == '__main__':
    unittest.main()
