class Node:

    def __init__(self, data, left = None, right = None):
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

    def contains(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.contains(data)
        elif data > self.data and self.right is not None:
            return self.right.contains(data)
        return None
