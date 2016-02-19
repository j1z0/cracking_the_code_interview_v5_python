'''simple stack implementation
it is bascially a linked list'''

class Node(object):
    '''
    The individual pieces of a linked list are the
    Nodes
    '''
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class Stack(object):
    def __init__(self, top = None):
        self.top = top 

    @property
    def empty(self):
        return self.top is None
   
    def push(self,data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        if self.top:
            retval = self.top.data
            self.top = self.top.next
            return retval

    def peek(self):
        if self.top:
            return self.top.data


if __name__ == "__main__":
    print("running tests")
    s = Stack( )
    s.push(10)
    assert 10 == s.peek()
    assert 10 == s.pop()
    assert None == s.pop()
    s.push(15)
    s.push(12)
    assert 12 == s.pop()
    assert 15 == s.pop()
    print("All good")

