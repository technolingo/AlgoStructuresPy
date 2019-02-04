#!/usr/bin/env python3
from queue import Queue


def weave(queue_one, queue_two):
    combined = Queue()

    while queue_one.peek() or queue_two.peek():
        if queue_one.peek():
            combined.enqueue(queue_one.dequeue())
        if queue_two.peek():
            combined.enqueue(queue_two.dequeue())

    return combined
