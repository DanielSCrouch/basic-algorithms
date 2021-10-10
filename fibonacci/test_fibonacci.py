import unittest

from fibonacci.fibonacci import *
from timer import timeit

class TestFibonacci(unittest.TestCase):

  def test_fibonacci(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 2)
    self.assertEqual(fibonacci(4), 3)
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(6), 8)

  @timeit
  def test_fibonacci(self):
    self.assertEqual(fibonacci(30), 832040)
    self.assertEqual(fibonacci(30), 832040)
    self.assertEqual(fibonacci(30), 832040)
    self.assertEqual(fibonacci(30), 832040)



