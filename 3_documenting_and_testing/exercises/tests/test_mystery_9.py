import unittest

from ..mystery_9 import sort_list

class TestMystery9(unittest.TestCase):
    """Tests the sorting function"""
    def already_sorted(self):
      """Tests if the function is already sorted"""
      actual = sort_list([1,2,3])
      expected = [1, 2, 3]
      self.assertEqual(actual,expected)
    def descending(self):
      """Tests if the function is in descending order"""
      actual = sort_list([8,5,2])
      expected = [2, 5, 8]
      self.assertEqual(actual,expected)
    def only_one_characters(self):
      """Tests if the function is already sorted"""
      actual = sort_list([1])
      expected = [1]
      self.assertEqual(actual,expected)
    def negative_number(self):
      """Tests if the function if there is a negative number"""
      actual = sort_list([6,-1,2,0,9])
      expected = [-1, 0, 2, 6, 9]
      self.assertEqual(actual,expected)
    def same_number(self):
      """Tests if the function if all is the same number"""
      actual = sort_list([10,10,10])
      expected = [10, 10, 10]
      self.assertEqual(actual,expected)
    def if_all_negative(self):
      """Tests if all is negative"""
      actual = sort_list([-9,-2,-10,-1])
      expected = [-10, -9, -2, -1]
      self.assertEqual(actual,expected)
    def if_not_numbers(self):
      """Test if list of characters was input"""
      actual = sort_list([a,b,c])
      expected = AssertionError
      self.assertEqual(actual,expected)
