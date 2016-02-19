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
        self.count = 1 if top else 0

    def push(self,data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.top:
            retval = Node(self.top.data)
            self.top = self.top.next
            self.count -= 1
            return retval

    def peek(self):
        if self.top:
            return self.top.data

class SetStack(object):

    def __init__(self, limit=10):
        self.limit = limit
        self.stacks =[]
        self.stacks.append(Stack())

    def push(self, data):
        stack = self.stacks[-1]
        if stack.count < self.limit:
            return stack.push(data)
        else:
            self.stacks.append(Stack())
            return self.push(data)
            

    def pop(self):
        stack = self.stacks[-1]
        if stack.count > 0:
            return stack.pop()
        else:
            self.stacks.pop()
            return self.pop()

    def popAt(self, index):
        stack = self.stacks[index]
        if stack.count > 0:
            return stack.pop()



if __name__ == "__main__":
    s = SetStack(2)
    s.push(10)
    assert 10 == s.stacks[-1].peek()
    s.push(9)
    assert 9 == s.stacks[-1].peek()
    s.push(8)
    assert 8 == s.stacks[-1].peek()
    assert 2 == len(s.stacks)
    assert 8 == s.pop().data
    assert 9 == s.pop().data
    assert 1 == len(s.stacks)
    assert 10 == s.pop().data

    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)

    assert 13 == s.popAt(0).data
    assert 15 == s.popAt(1).data

    print("All good")

