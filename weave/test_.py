from .queue import Queue
from .index import weave


class TestWeaveFunction():

    def setup_method(self):
        self.queue_one = Queue()
        self.queue_one.enqueue(1)
        self.queue_one.enqueue(2)
        self.queue_one.enqueue(3)

        self.queue_two = Queue()
        self.queue_two.enqueue('hi')
        self.queue_two.enqueue('nihao')
        self.queue_two.enqueue('hola')

    def test_weave(self):
        result = weave(self.queue_one, self.queue_two)

        assert result.dequeue() == 1
        assert result.dequeue() == 'hi'
        assert result.dequeue() == 2
        assert result.dequeue() == 'nihao'
        assert result.dequeue() == 3
        assert result.dequeue() == 'hola'
