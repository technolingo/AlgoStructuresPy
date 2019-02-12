'''
Create a queue data structure.  The queue
should be a class with methods 'enqueue' and 'dequeue'.
--- Examples
    q = Queue()
    q.enqueue(1)
    q.dequeue() # returns 1;
'''


class Queue:
    ''' A rudimentary queue '''

    def __init__(self):
        self.lst = []

    def enqueue(self, elem):
        self.lst.insert(0, elem)

    def dequeue(self):
        try:
            return self.lst.pop()
        except:
            return None

    def __repr__(self):
        return str(self.lst)
