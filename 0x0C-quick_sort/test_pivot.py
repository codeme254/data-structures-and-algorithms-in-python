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
        pivot_idx = pivot(list, 0, len(list)-1)
        self.assertEqual(pivot_idx, 2)
    
    def test_list_with_negative_integers(self):
        list = [-2, -8, -1, -9, -12]
        pivot_idx = pivot(list, 0, len(list)-1)
        self.assertEqual(pivot_idx, 3)
    
    def test_with_floating_point_positive_value(self):
        list = [2.5, 2.8, 1.2, 3, 2.2]
        pivot_idx = pivot(list, 0, len(list)-1)
        self.assertEqual(pivot_idx, 2)
    
    def test_with_negative_floating_point_values(self):
        list = [-2.5, -2.8, -1.2, -3, -2.2]
        pivot_idx = pivot(list, 0, len(list)-1)
        self.assertEqual(pivot_idx, 2)
    
    def test_with_strings(self):
        list = ["Ball", "Art", "Alien", "Craft", "JigSaw"]
        pivot_idx = pivot(list, 0, len(list)-1)
        self.assertEqual(pivot_idx, 2)

if __name__ == "__main__":
    unittest.main()