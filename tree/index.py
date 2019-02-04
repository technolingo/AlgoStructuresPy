class Node:

    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def add(self, data):
        ''' add a child to the instance with provided data.'''
        child = Node(data, [])
        self.children.append(child)

    def remove(self, data):
        ''' remove all children containing the given data.'''
        self.children = list(filter(lambda node: node.data != data, self.children))


class Tree:

    def __init__(self, root = None):
        self.root = root

    def traverse_breadth(self, func):
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            nodes.extend(node.children)
            func(node)

    def traverse_depth(self, func):
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            nodes[0:0] = node.children
            func(node)
