#!/usr/bin/env python3
from unittest import TestCase

from queue import Queue
from index import weave

class WeaveFunctionTestCase(TestCase):

    def setUp(self):
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
        self.assertEqual(result.dequeue(), 1)
        self.assertEqual(result.dequeue(), 'hi')
        self.assertEqual(result.dequeue(), 2)
        self.assertEqual(result.dequeue(), 'nihao')
        self.assertEqual(result.dequeue(), 3)
        self.assertEqual(result.dequeue(), 'hola')
