from .linkedlist import LinkedList
from .index import get_nth_node_from_last


class TestFromLast():

    def setup_method(self):
        self.llst = LinkedList()

    def test_empty(self):
        assert get_nth_node_from_last(self.llst, 5) is None

    def test_zeroth(self):
        self.llst.insert_last('a')
        self.llst.insert_last('b')
        assert get_nth_node_from_last(self.llst, 0).data == 'a'

    def test_normal(self):
        self.llst.insert_last('a')
        self.llst.insert_last('b')
        self.llst.insert_last('c')
        self.llst.insert_last('d')
        self.llst.insert_last('e')
        self.llst.insert_last('f')
        self.llst.insert_last('g')
        assert get_nth_node_from_last(self.llst, 2).data == 'e'
        assert get_nth_node_from_last(self.llst, 4).data == 'c'
        assert get_nth_node_from_last(self.llst, 5).data == 'b'
