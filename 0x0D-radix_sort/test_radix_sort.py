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
