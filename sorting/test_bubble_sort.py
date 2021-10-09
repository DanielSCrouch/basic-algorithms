import unittest

from timer import timeit
from sorting.bubble_sort import *

class TestSort(unittest.TestCase):

  @timeit
  def test_bubble_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] 
    bubble_sort(basket) 
    self.assertEqual(basket, [1, 2, 3, 4, 5, 6, 7, 8])

  @timeit
  def test_selection_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4, 0] 
    selection_sort(basket) 
    self.assertEqual(basket, [0, 1, 2, 3, 4, 5, 6, 7, 8])

  @timeit
  def test_insertion_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] 
    basket = insertion_sort(basket) 
    self.assertEqual(basket, [1, 2, 3, 4, 5, 6, 7, 8])

  @timeit
  def test_merge_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] 
    basket = merge_sort(basket) 
    self.assertEqual(basket, [1, 2, 3, 4, 5, 6, 7, 8])