from .linkedlist import LinkedList
from .index import midpoint


class TestMidpoint():

    def setup_method(self):
        self.llst = LinkedList()

    def test_empty(self):
        assert midpoint(self.llst) is None

    def test_odd(self):
        self.llst.insert_last('a')
        assert len(self.llst) == 1
        assert midpoint(self.llst).data == 'a'

        self.llst.insert_last('b')
        self.llst.insert_last('c')
        assert len(self.llst) == 3
        assert midpoint(self.llst).data == 'b'

        self.llst.insert_last('d')
        self.llst.insert_last('e')
        assert len(self.llst) == 5
        assert midpoint(self.llst).data == 'c'

        self.llst.insert_last('f')
        self.llst.insert_last('g')
        self.llst.insert_last('h')
        self.llst.insert_last('i')
        assert len(self.llst) == 9
        assert midpoint(self.llst).data == 'e'

    def test_even(self):
        self.llst.insert_last('a')
        self.llst.insert_last('b')
        assert len(self.llst) == 2
        assert midpoint(self.llst).data == 'a'

        self.llst.insert_last('c')
        self.llst.insert_last('d')
        assert len(self.llst) == 4
        assert midpoint(self.llst).data == 'b'

        self.llst.insert_last('e')
        self.llst.insert_last('f')
        self.llst.insert_last('g')
        self.llst.insert_last('h')
        assert len(self.llst) == 8
        assert midpoint(self.llst).data == 'd'
