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
