'''
Given a root node, validate the binary search tree,
ensuring that every node's left hand child is
less than the parent node's value, and that
every node's right hand child is greater than
the parent
'''


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data == self.data:
            raise NotImplemented
        elif data < self.data and self.left is None:
            self.left = Node(data)
        elif data > self.data and self.right is None:
            self.right = Node(data)
        elif data < self.data:
            self.left.insert(data)
        elif data > self.data:
            self.right.insert(data)
        else:
            raise Exception('Unexpected edge case')


def is_binary_search_tree(node, min=None, max=None):
    ''' Inital node is the root. Duplicates are not allowed. '''
    if node is None:
        return False
    if min is not None and node.data <= min:
        return False
    if max is not None and node.data >= max:
        return False
    if node.left is not None:
        return is_binary_search_tree(node.left, min, node.data)
    if node.right is not None:
        return is_binary_search_tree(node.right, node.data, max)
    return True
