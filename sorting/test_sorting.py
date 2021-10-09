import unittest

from timer import timeit
from sorting.sorting import *

class TestSort(unittest.TestCase):
  r = 500
  sorted = [1] * r + [2] * r + [3] * r + [4] * r + [5] * r + [6] * r + [7] * r + [8] * r

  @timeit
  def test_bubble_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] * self.r
    bubble_sort(basket) 
    self.assertEqual(basket, self.sorted)

  @timeit
  def test_selection_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] * self.r
    selection_sort(basket) 
    self.assertEqual(basket, self.sorted)

  @timeit
  def test_insertion_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] * self.r
    basket = insertion_sort(basket) 
    self.assertEqual(basket, self.sorted)

  @timeit
  def test_merge_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] * self.r
    basket = merge_sort(basket) 
    self.assertEqual(basket, self.sorted)

  @timeit
  def test_quick_sort(self):
    basket = [6, 5, 3, 1, 8, 7, 2, 4] * self.r
    basket = quick_sort(basket) 
    self.assertEqual(basket, self.sorted)

