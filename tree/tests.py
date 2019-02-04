from unittest import TestCase, skip
import gc

from index import Tree, Node


class TreeTestCase(TestCase):

    def setUp(self):
        self.node = Node('a')
        self.tree = Tree()

    def tearDown(self):
        ''' tearDown doesn't seem to be able to delete lists created in
            each test, thus resulting errors if each test is not run seperately.
            will come back to this when a better solution is found.
        '''
        self.node.children = []
        self.node = None
        del self.node
        gc.collect()

    @skip
    def test_node_properties(self):
        self.assertEqual(self.node.data, 'a')
        self.assertEqual(self.node.children, [])
        self.assertEqual(len(self.node.children), 0)

    @skip
    def test_node_add_children(self):
        self.node.add('b')
        self.assertEqual(len(self.node.children), 1)
        self.assertEqual(self.node.children[0].data, 'b')
        self.assertEqual(len(self.node.children[0].children), 0)

    @skip
    def test_node_remove_children(self):
        self.node.add('b')
        self.node.add('b')
        self.node.add('c')
        self.assertEqual(len(self.node.children), 3)
        self.node.remove('b')
        self.assertEqual(len(self.node.children), 1)
        self.assertEqual(self.node.children[0].data, 'c')

    @skip
    def test_tree_properties(self):
        self.assertIsNone(self.tree.root)

    @skip
    def test_tree_traverse_breadth(self):
        letters = []
        self.tree.root = self.node
        self.tree.root.add('b')
        self.tree.root.add('c')
        self.tree.root.children[0].add('d')

        def f(node): letters.append(node.data)
        self.tree.traverse_breadth(f)
        self.assertEqual(letters, ['a', 'b', 'c', 'd'])

    @skip
    def test_tree_traverse_depth(self):
        letters = []
        self.tree.root = self.node
        self.tree.root.add('b')
        self.tree.root.add('d')
        self.tree.root.children[0].add('c')

        def f(node): letters.append(node.data)
        self.tree.traverse_depth(f)
        self.assertEqual(letters, ['a', 'b', 'c', 'd'])
