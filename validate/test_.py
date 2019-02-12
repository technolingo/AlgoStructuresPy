from .index import Node, is_binary_search_tree


class TestBinarySearchTreeValidator():

    def test_valid(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        assert is_binary_search_tree(n) is True

    def test_invalid(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        n.left.left.right = Node(999)
        assert is_binary_search_tree(n) is False
