'''simple queue implementation
it is bascially a linked list that tracks first
and last nodes'''

class Node(object):
    '''
    The individual pieces of a linked list are the
    Nodes
    '''
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class Stack(object):
    def __init__(self, first = None):
        self.first = first 
        self.last = first 

    def enqueue(self,data):
        new_node = Node(data)
        if not self.first:
            self.last = new_node
            self.first = self.last
        else:
            self.last.next = new_node
            self.last = self.last.next

    def dequeue(self):
        if self.first:
            retval = self.first.data
            self.first = self.first.next
            return retval


if __name__ == "__main__":
    print("running tests")
    s = Stack()
    s.enqueue(10)
    assert 10 == s.dequeue()
    assert None == s.dequeue()
    s.enqueue(15)
    s.enqueue(12)
    assert 15 == s.dequeue()
    assert 12 == s.dequeue()
    print("All good")

