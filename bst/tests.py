from unittest import TestCase, skip

from index import Node


class BinarySearchTreeTestCase(TestCase):

    def test_insert(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(17)

        self.assertEqual(node.left.data, 5)
        self.assertEqual(node.right.data, 15)
        self.assertEqual(node.right.right.data, 17)

    def test_contains_found_node(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)

        three = node.left.left.right
        self.assertEqual(node.contains(3), three)

    def test_contains_return_none(self):
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)

        self.assertIsNone(node.contains(9999))
