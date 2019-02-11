import gc
import pytest

from .index import Tree, Node


class TestTree():

    def setup_method(self):
        self.node = Node('a')
        self.tree = Tree()

    def teardown_method(self):
        ''' tearDown doesn't seem to be able to delete lists created in
            each test, thus resulting errors if each test is not run seperately.
            will come back to this when a better solution is found.
        '''
        self.node.children = []
        self.node = None
        del self.node
        gc.collect()

    def test_node_properties(self):
        assert self.node.data == 'a'
        assert self.node.children == []
        assert len(self.node.children) == 0

    def test_node_add_children(self):
        self.node.add('b')
        assert len(self.node.children) == 1
        assert self.node.children[0].data == 'b'
        assert len(self.node.children[0].children) == 0

    @pytest.mark.skip
    def test_node_remove_children(self):
        self.node.add('b')
        self.node.add('b')
        self.node.add('c')
        assert len(self.node.children) == 3
        self.node.remove('b')
        assert len(self.node.children) == 1
        assert self.node.children[0].data == 'c'

    @pytest.mark.skip
    def test_tree_properties(self):
        self.assertIsNone(self.tree.root)

    @pytest.mark.skip
    def test_tree_traverse_breadth(self):
        letters = []
        self.tree.root = self.node
        self.tree.root.add('b')
        self.tree.root.add('c')
        self.tree.root.children[0].add('d')

        def f(node): letters.append(node.data)
        self.tree.traverse_breadth(f)
        assert letters == ['a', 'b', 'c', 'd']

    @pytest.mark.skip
    def test_tree_traverse_depth(self):
        letters = []
        self.tree.root = self.node
        self.tree.root.add('b')
        self.tree.root.add('d')
        self.tree.root.children[0].add('c')

        def f(node): letters.append(node.data)
        self.tree.traverse_depth(f)
        assert letters == ['a', 'b', 'c', 'd']
