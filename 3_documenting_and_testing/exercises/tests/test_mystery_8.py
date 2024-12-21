import unittest

from ..mystery_8 import searching

class TestMystery8(unittest.TestCase):
    """
     Tests the function searching
       """
    def input_was_capital(self):
        """if the character in the list was capital """
        actual= searching(['hiba','Daffallah','Ice cream'],'i')
        expected=  ['hiba', 'Ice cream']
        self.assertEqual(actual,expected)
    def searching_for_words(self):
       """If searching for a word """
       actual= searching(['hiba','Daffallah','Ice cream'],'i')
       expected=  ['hiba', 'Ice cream']
       self.assertEqual(actual,expected)
    def list_has_numbers(self):
       """If list has numbers """
       actual= searching(['wafaa',123,'Juice'],'j')
       expected=  ['juice']
       self.assertEqual(actual,expected)
    def to_search_capital(self):
        """searching for a capital letter"""
        actual= searching(['wafaa','ibrahim','Mohammed'],'M')
        expected=  ['ibrahim', 'Mohammed']
        self.assertEqual(actual,expected)
    
