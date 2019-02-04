from unittest import TestCase, skip

from index import Node, is_binary_search_tree


class BinarySearchTreeValidatorTestCase(TestCase):

    def test_valid(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        self.assertTrue(is_binary_search_tree(n))

    def test_invalid(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        n.left.left.right = Node(999)
        self.assertFalse(is_binary_search_tree(n))
