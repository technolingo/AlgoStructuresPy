class Node:

    def __init__(self, data, children = []):
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


# the below two 'tests' must be run seperately to avoid
# Python implementation issues regarding mutable objects

# root = Node(0)
# root.add(1)
# root.add(2)
# root.add(3)
# root.children[0].add(4)
# root.children[2].add(5)
#
# print("{} =?= {}".format([1, 3, 2], get_level_width(root)))

rt = Node(0)
rt.add(1)
rt.children[0].add(2)
rt.children[0].add(3)
rt.children[0].children[0].add(4)

print("{} =?= {}".format([1, 1, 2, 1], get_level_width(rt)))
