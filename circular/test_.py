from .linkedlist import LinkedList, Node
from .index import is_circular


class TestIsCircular():

    def test_circular(self):
        d = Node('d')
        c = Node('c', d)
        b = Node('b', c)
        a = Node('a', b)
        d.next = b
        llst = LinkedList(a)

        assert llst.get_first().data == 'a'
        assert llst.get_first().next == b
        assert is_circular(llst) is True

    def test_non_circular(self):
        d = Node('d')
        c = Node('c', d)
        b = Node('b', c)
        a = Node('a', b)
        llst = LinkedList(a)

        assert llst.get_first().data == 'a'
        assert llst.get_first().next == b
        assert is_circular(llst) is False
