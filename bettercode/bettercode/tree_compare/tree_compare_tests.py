import unittest

from bettercode.bettercode.tree_compare.tree_compare import compare_nodes, Node


class TreeCompareTests(unittest.TestCase):
  def test_empty_trees(self):
    """
    A                             B
    EMPTY TREE                    EMPTY TREE
    """
    self.assertTrue(compare_nodes(None, None))

  def test_one_empty_tree(self):
    """
    A                             B
    EMPTY TREE                    1
    """
    b = Node(val=1, left=None, right=None)
    self.assertFalse(compare_nodes(None, b))

  def test_equality_one_level(self):
    """
    Values and structure are both the same
    A                             B
    1                             1
    """
    a = Node(val=1, left=None, right=None)
    b = Node(val=1, left=None, right=None)
    self.assertTrue(compare_nodes(a, b))

  def test_inequality_one_level(self):
    """
    Structure is the same, values are different
    A                             B
    1                             2
    """
    a = Node(val=1, left=None, right=None)
    b = Node(val=2, left=None, right=None)
    self.assertFalse(compare_nodes(a, b))

  def test_equality_one_branch(self):
    """
    A                             B
        1                            1
       /                            /
      2                            2
    """
    a2 = Node(val=2, left=None, right=None)
    a1 = Node(val=1, left=a2, right=None)
    b2 = Node(val=2, left=None, right=None)
    b1 = Node(val=1, left=b2, right=None)
    self.assertTrue(compare_nodes(a1, b1))

    # Not necessary but the second level should also be true
    self.assertTrue(compare_nodes(a2, b2))

  def test_equality_2_levels(self):
    """
    A                             B
        1                            1
       / \                          / \
      2   3                        2   3
           \                            \
            4                            4
    """
    a4 = Node(val=4, left=None, right=None)
    a2 = Node(val=2, left=None, right=None)
    a3 = Node(val=3, left=None, right=a4)
    a1 = Node(val=1, left=a2, right=a3)

    b4 = Node(val=4, left=None, right=None)
    b2 = Node(val=2, left=None, right=None)
    b3 = Node(val=3, left=None, right=b4)
    b1 = Node(val=1, left=b2, right=b3)
    self.assertTrue(compare_nodes(a1, b1))


  def test_inequality_2_levels(self):
    """
    Structure is the same, values are different

    A                             B
        1                            1
       / \                          / \
      2   3                        2   3
           \                            \
            5                            4
    """
    a5 = Node(val=5, left=None, right=None)
    a2 = Node(val=2, left=None, right=None)
    a3 = Node(val=3, left=None, right=a5)
    a1 = Node(val=1, left=a2, right=a3)

    b4 = Node(val=4, left=None, right=None)
    b2 = Node(val=2, left=None, right=None)
    b3 = Node(val=3, left=None, right=b4)
    b1 = Node(val=1, left=b2, right=b3)
    self.assertFalse(compare_nodes(a1, b1))

  def test_inequality_multi_levels(self):
    """
    Structure is different
    A                             B
        1                            1
       / \                          /
      2   3                        2
    """
    a2 = Node(val=2, left=None, right=None)
    a3 = Node(val=3, left=None, right=None)
    a1 = Node(val=1, left=a2, right=a3)

    b2 = Node(val=2, left=None, right=None)
    b1 = Node(val=1, left=b2, right=None)
    self.assertFalse(compare_nodes(a1, b1))


