import pytest

from .index import LinkedList, Node


class TestLinkedList():

    def setup_method(self):
        self.llst = LinkedList()

    def test_node_class(self):
        node_a = Node(1)
        assert isinstance(node_a, Node) is True
        assert node_a.data == 1
        assert node_a.next is None

        node_b = Node('a', node_a)
        assert isinstance(node_b, Node) is True
        assert node_b.data == 'a'
        assert node_b.next == node_a

        node_c = Node(['a'])
        assert isinstance(node_c, Node) is True
        assert node_c.data == ['a']
        assert node_c.next is None

    def test_linkedlist_class(self):
        assert isinstance(self.llst, LinkedList) is True
        assert self.llst.head is None

    def test_size(self):
        assert self.llst.size() == 0
        self.llst.insert_first(1)
        assert self.llst.size() == 1
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        assert self.llst.size() == 4
        assert len(self.llst) == 4

    def test_clear(self):
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        self.llst.insert_first(1)
        assert self.llst.size() == 4
        self.llst.clear()
        assert self.llst.size() == 0

    def test_get_at(self):
        assert self.llst.get_at(-10) is None
        self.llst.insert_last(1)
        assert self.llst.get_at(0).data == 1
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        assert self.llst.get_at(2).data == 3
        assert self.llst.get_at(7) is None

    def test_get_first(self):
        assert self.llst.get_first() is None
        self.llst.insert_first(1)
        assert self.llst.get_first().data == 1
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        assert self.llst.get_first().data == 3

    def test_get_last(self):
        assert self.llst.get_last() is None
        self.llst.insert_first(1)
        assert self.llst.get_last().data == 1
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        assert self.llst.get_last().data == 1

    def test_insert_at(self):
        # empty
        self.llst.insert_at(0, 'hi')
        assert self.llst.get_at(0).data == 'hi'
        # out of the lower bound -> prepend
        self.llst.insert_last(2)
        self.llst.insert_at(-10, 'nihao')
        assert self.llst.get_at(0).data == 'nihao'
        assert self.llst.get_at(1).data == 'hi'
        assert self.llst.get_at(2).data == 2
        # in the middle
        self.llst.insert_at(1, 9)
        assert self.llst.get_at(0).data == 'nihao'
        assert self.llst.get_at(1).data == 9
        assert self.llst.get_at(2).data == 'hi'
        assert self.llst.get_at(3).data == 2
        # out of the upper bound -> append
        self.llst.insert_at(99, 'asdf')
        assert self.llst.get_at(4).data == 'asdf'
        assert self.llst.get_last().data == 'asdf'
        assert self.llst.get_at(99) is None

    def test_insert_first(self):
        self.llst.insert_first(1)
        assert self.llst.head.data == 1
        self.llst.insert_first(2)
        assert self.llst.head.data == 2

    def test_insert_last(self):
        self.llst.insert_last(1)
        assert self.llst.get_last().data == 1
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        assert self.llst.get_last().data == 3

    def test_remove_at(self):
        # empty
        try:
            self.llst.remove_at(4)
        except Exception as e:
            pytest.fail(e)
        # one
        self.llst.insert_last(1)
        self.llst.remove_at(0)
        assert self.llst.get_at(0) is None
        # multiple
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.llst.insert_last(4)
        self.llst.remove_at(1)
        assert self.llst.get_at(1).data == 4
        # out of the lower bound -> ignore
        try:
            self.llst.remove_at(-4)
        except Exception as e:
            pytest.fail(e)
        assert self.llst.get_at(1).data == 4
        # out of the upper bound -> ignore
        try:
            self.llst.remove_at(19)
        except Exception as e:
            pytest.fail(e)
        assert self.llst.get_at(1).data == 4

    def test_remove_first(self):
        # empty
        try:
            self.llst.remove_first()
        except Exception as e:
            pytest.fail(e)
        # one element
        self.llst.insert_first(1)
        self.llst.remove_first()
        assert self.llst.get_first() is None
        # multiple elements
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        self.llst.insert_first(4)
        assert self.llst.get_first().data == 4
        self.llst.remove_first()
        assert self.llst.get_first().data == 3

    def test_remove_last(self):
        # empty
        try:
            self.llst.remove_last()
        except Exception as e:
            pytest.fail(e)
        # one
        self.llst.insert_first(1)
        self.llst.remove_last()
        assert self.llst.get_last() is None
        # multiple
        self.llst.insert_first(2)
        self.llst.insert_first(3)
        self.llst.insert_first(4)
        assert self.llst.get_last().data == 2
        self.llst.remove_last()
        assert self.llst.get_last().data == 3

    def test_every(self):
        self.llst.insert_last(1)
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.llst.insert_last(4)
        try:
            def f(node): node.data += 10
            self.llst.every(f)
        except Exception as e:
            pytest.fail(e)
        assert self.llst.get_at(0).data == 11
        assert self.llst.get_at(1).data == 12
        assert self.llst.get_at(2).data == 13
        assert self.llst.get_at(3).data == 14

    def test_iteration(self):
        ''' make it compatible with for-loops & next() function '''
        # empty
        try:
            for node in self.llst:
                node.data += 10
        except Exception as e:
            pytest.fail(e)
        assert self.llst.get_first() is None
        # multiple
        self.llst.insert_last(1)
        self.llst.insert_last(2)
        self.llst.insert_last(3)
        self.llst.insert_last(4)
        # next() function
        g = iter(self.llst)
        assert next(g).data == 1
        assert next(g).data == 2
        assert next(g).data == 3
        assert next(g).data == 4
        # for-loop
        try:
            for node in self.llst:
                node.data += 10
        except Exception as e:
            pytest.fail(e)
        assert self.llst.get_at(0).data == 11
        assert self.llst.get_at(1).data == 12
        assert self.llst.get_at(2).data == 13
        assert self.llst.get_at(3).data == 14
