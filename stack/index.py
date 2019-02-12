'''
Create a stack data structure.  The stack
should be a class with methods 'push', 'pop', and
'peek'.  Adding an element to the stack should
store it until it is removed.
--- Examples
  const s = new Stack();
  s.push(1);
  s.push(2);
  s.pop(); // returns 2
  s.pop(); // returns 1
'''


class Stack:

    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        try:
            return self.data.pop()
        except:
            return None

    def peek(self):
        try:
            return self.data[-1]
        except:
            return None
