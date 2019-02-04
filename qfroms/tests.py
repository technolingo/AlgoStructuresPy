from unittest import TestCase

from index import Queue


class QueueFromStacksTestCase(TestCase):

    def setUp(self):
        self.q = Queue()

    def test_enqueue(self):
        try:
            self.q.enqueue(1)
        except Exception as e:
            self.fail(e)

    def test_dequeue(self):
        try:
            self.q.enqueue(1)
            self.assertEqual(self.q.dequeue(), 1)
        except Exception as e:
            self.fail(e)

    def test_order(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertEqual(self.q.dequeue(), 1)
        self.assertEqual(self.q.dequeue(), 2)
        self.assertEqual(self.q.dequeue(), 3)
