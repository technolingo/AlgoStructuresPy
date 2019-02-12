'''
Given a linked list, return true if the list
is circular, false if it is not.
--- Examples
  const l = new List();
  const a = new Node('a');
  const b = new Node('b');
  const c = new Node('c');
  l.head = a;
  a.next = b;
  b.next = c;
  c.next = b;
  circular(l) true
'''


def is_circular(llst):
    '''checks if a linked list is circular'''
    if llst.head is None or llst.head.next is None:
        return False

    slow = fast = llst.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
