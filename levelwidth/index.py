'''
Given the root node of a tree, return
an array where each element is the width
of the tree at each level.
--- Example
    Given:
        0
      / |  \
    1   2   3
    |       |
    4       5
    Answer: [1, 3, 2]
'''


class Node:

    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def add(self, data):
        ''' add a child to the instance with provided data.'''
        child = Node(data, [])
        self.children.append(child)


def get_level_width(root):
    output = [0]
    nodes = [root, 'x']

    while len(nodes) > 1:
        node = nodes.pop(0)
        if node == 'x':
            nodes.append('x')
            output.append(0)
        else:
            output[-1] += 1
            nodes.extend(node.children)

    return output
