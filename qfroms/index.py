class Stack:

    def __init__(self):
        self._data = []

    def push(self, elem):
        self._data.append(elem)

    def pop(self):
        try:
            return self._data.pop()
        except:
            return None

    def peek(self):
        try:
            return self._data[-1]
        except:
            return None


class Queue:

    def __init__(self):
        self._stack_one = Stack()
        self._stack_two = Stack()

    def _reverse(self):
        while self._stack_one.peek():
            self._stack_two.push(self._stack_one.pop())

    def enqueue(self, elem):
        self._stack_one.push(elem)

    def dequeue(self):
        self._reverse()
        return self._stack_two.pop()

    def peek(self):
        self._reverse()
        return self._stack_two.peek()
