import unittest

from ..is_in_both import is_in_both

class TestCountBetween(unittest.TestCase):
    """Test suite for the is_in_both function"""

    # Standard test cases
    def the_string_is_in_all_items(self):
        """the string is in both lists"""
        self.assertEqual(is_in_both(['game','Game'],['game','Games'],'game'),True)
    def string_in_one_item_in_lists(self):
        """the string is in one items"""
        self.assertEqual(is_in_both(['Good','december'],['Good','january'],'Good'),True)
    def not_found(self):
        """the string is not in the list"""
        self.assertEqual(is_in_both(['code','data'],['test','plan'],'sum'),False)
