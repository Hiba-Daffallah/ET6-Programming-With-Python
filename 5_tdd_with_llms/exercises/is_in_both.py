""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.
"""


 
def is_in_both(pool_1,pool_2,search_for) -> bool:
 """
  this function will search for a string in two list of strings and
  returns true if it's in both of them.

  Parameters:
  search_for: the string required to search for
  pool_1: the first list to look for 'search_for' string in
  pool_2: the second list to look for 'search_for' string in

  Returns:
  True/False if the string was/wasn't in both lists

  Raises: AssertionError 
  if items where not strings

 >>> is_in_both(['game','Game'],['game','Games'],'game')
 True
 >>> is_in_both(['Good','december'],['Good','january'],'Good')
 True
 >>> is_in_both(['code','data'],['test','plan'],'sum')
 False

 """
 assert isinstance(pool_1, list)
 assert isinstance(pool_2, list)
 assert isinstance(search_for, str)
 temp = (search_for in pool_1) and (search_for in pool_2)
 return  temp
