from .index import Node, get_level_width


def test_get_level_width():
    root = Node(0)
    assert get_level_width(root) == [1]
    root.add(1)
    root.children[0].add(2)
    root.children[0].add(3)
    root.children[0].children[0].add(4)
    assert get_level_width(root) == [1, 1, 2, 1]
    root.children[0].children[0].add(5)
    root.children[0].children[0].add(5)
    assert get_level_width(root) == [1, 1, 2, 3]
