import unittest
from binary_tree.binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):

  def test_breadth_first_traversal(self):
    bt = BinaryTree() 
    bt.insert(9) 
    bt.insert(4)
    bt.insert(6)
    bt.insert(20)
    bt.insert(170)
    bt.insert(15)
    bt.insert(1)

    ordered = [9, 4, 20, 1, 6, 15, 170]
    traversal = bt.breadth_first_traversal()
    for item in ordered:
      self.assertEqual(item, traversal.__next__())
      
  def test_breadth_first_traversal2(self):
    bt = BinaryTree() 
    bt.insert(9) 
    bt.insert(4)
    bt.insert(6)
    bt.insert(20)
    bt.insert(170)
    bt.insert(15)
    bt.insert(2)
    bt.insert(1)
    bt.insert(3)
    bt.insert(5)
    bt.insert(7)
    bt.insert(14)
    bt.insert(16)
    bt.insert(150)
    bt.insert(171)

    ordered =  [9, 4, 20, 2, 6, 15, 170, 1, 3, 5, 7, 14, 16, 150, 171]
    traversal = bt.breadth_first_traversal()
    for item in ordered:
      self.assertEqual(item, traversal.__next__())

  def test_depth_first_traversal_preorder(self):
    bt = BinaryTree() 
    bt.insert(9) 
    bt.insert(4)
    bt.insert(6)
    bt.insert(20)
    bt.insert(170)
    bt.insert(15)
    bt.insert(1)

    ordered = [9, 4, 1, 6, 20, 15, 170]
    traversal = bt.depth_first_traversal(order="preorder")
    for item in ordered:
      self.assertEqual(item, traversal.__next__())
  
  def test_depth_first_traversal_inorder(self):
    bt = BinaryTree() 
    bt.insert(9) 
    bt.insert(4)
    bt.insert(6)
    bt.insert(20)
    bt.insert(170)
    bt.insert(15)
    bt.insert(1)

    ordered = [1, 4, 6, 9, 15, 20, 170]
    traversal = bt.depth_first_traversal(order="inorder")
    for item in ordered:
      self.assertEqual(item, traversal.__next__())

  # def test_depth_first_traversal_postorder(self):
    # bt = BinaryTree() 
    # bt.insert(9) 
    # bt.insert(4)
    # bt.insert(6)
    # bt.insert(20)
    # bt.insert(170)
    # bt.insert(15)
    # bt.insert(1)

    # ordered = [1, 6, 4, 15, 170, 20, 9]
    # traversal = bt.depth_first_traversal(order="postorder")
    # for item in ordered:
    #   self.assertEqual(item, traversal.__next__())
