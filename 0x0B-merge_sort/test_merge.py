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