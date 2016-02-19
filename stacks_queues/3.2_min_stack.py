'''simple stack implementation
it is bascially a linked list'''
from stack import Stack
import sys

class Node(object):
    '''
    The individual pieces of a linked list are the
    Nodes
    '''
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class StackWithMin(object):
    def __init__(self, top = None):
        self.top = top 

        #store the min values
        self._min = Stack(top) 

    def min(self):
        retval = self._min.peek()
        if retval is None:
            retval = sys.maxsize
        return retval



    def push(self,data):
        new_node = Node(data, self.top)
        self.top = new_node

        if data <= self.min(): 
            self._min.push(data)


    def pop(self):
        if self.top:
            retval = Node(self.top.data)
            self.top = self.top.next

            if retval.data == self.min():
                self._min.pop()
            return retval

    def peek(self):
        if self.top:
            return self.top.data


if __name__ == "__main__":
    s = StackWithMin()
    s.push(10)
    assert s.min() == 10
    s.push(5)
    assert s.min() == 5
    s.push(4)
    assert s.min() == 4
    s.pop()
    assert s.min() == 5
    s.pop()
    assert s.min() == 10
    print("All good")

