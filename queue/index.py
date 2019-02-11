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
