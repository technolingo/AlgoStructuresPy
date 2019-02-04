class Stack:

    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        try:
            return self.data.pop()
        except:
            return None

    def peek(self):
        try:
            return self.data[-1]
        except:
            return None
