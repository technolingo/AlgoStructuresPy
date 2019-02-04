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


q = Queue()
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
q.enqueue(3)
print(q)
print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
