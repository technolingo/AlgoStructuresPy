from .index import Queue


class TestQueue:

    def setup_method(self):
        self.q = Queue()

    def enqueue_one_to_three(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

    def test_enqueue(self):
        self.enqueue_one_to_three()
        assert self.q.lst == [3, 2, 1]
        self.q.enqueue(5)
        assert self.q.lst == [5, 3, 2, 1]

    def test_dequeue(self):
        self.enqueue_one_to_three()
        assert self.q.dequeue() == 1
        assert self.q.dequeue() == 2
        assert self.q.dequeue() == 3
        assert self.q.dequeue() is None
