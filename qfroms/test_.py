import pytest

from .index import Queue


class TestQueueFromStacks():

    def setup_method(self):
        self.q = Queue()

    def enqueue_one_to_three(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

    def test_enqueue(self):
        try:
            self.q.enqueue(1)
        except Exception as e:
            pytest.fail(e)

    def test_dequeue(self):
        try:
            self.q.enqueue(1)
            assert self.q.dequeue() == 1
        except Exception as e:
            pytest.fail(e)

    def test_order_fifo(self):
        self.enqueue_one_to_three()
        assert self.q.dequeue() == 1
        assert self.q.dequeue() == 2
        assert self.q.dequeue() == 3

    def test_peek(self):
        self.enqueue_one_to_three()
        assert self.q.peek() == 1
        assert self.q.dequeue() == 1
        assert self.q.peek() == 2
        assert self.q.dequeue() == 2
