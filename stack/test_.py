from .index import Stack


class TestStack:

    def setup_method(self):
        self.s = Stack()

    def push_one_to_three(self):
        self.s.push(1)
        self.s.push(2)
        self.s.push(3)

    def test_push_pop(self):
        self.s.push(1)
        assert self.s.pop() == 1
        self.s.push(2)
        assert self.s.pop() == 2

    def test_order_filo(self):
        self.push_one_to_three()
        assert self.s.pop() == 3
        assert self.s.pop() == 2
        assert self.s.pop() == 1

    def test_peek(self):
        self.push_one_to_three()
        assert self.s.peek() == 3
        assert self.s.pop() == 3
        assert self.s.peek() == 2
        assert self.s.pop() == 2
        assert self.s.peek() == 1
