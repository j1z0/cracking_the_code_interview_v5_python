'''
Describe how you could use a single array to implement three stack
'''

class Node(object):
    '''
    The individual pieces of a linked list are the
    Nodes
    '''
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class Stack(object):
    def __init__(self):
        self.stack = ['-'] * 3

    def get_top(self, stack_no):
        #TODO: cache stack_tops to avoid the lookup
        top_idx = -4 + stack_no
        while True:
            try:
                top_val = self.stack[top_idx]
            except IndexError:
                top_idx += 3
                break

            if top_val == "-":
                top_idx -= 3
            else:
                break

        return top_idx

    def is_empty(self, node_index):
        return self.stack[node_index] == '-'

    def grow_stack(self):
        self.stack.extend(['-','-','-'])

    def stack_has_space(self, top_idx):
        return top_idx < -3



    def push(self,data,stack_no):
        '''
        stack_no denotes the stack to push on
        so we don't have to keep reorganizing the array
        push and pop from the end of the array
        '''
        top = self.get_top(stack_no)
        print("stack top is ", top)
        if self.is_empty(top):
            print("stack is empty")
            self.stack[top] = data
        else:
            if not self.stack_has_space(top):
                print("growing stack")
                self.grow_stack()
                self.stack[top] = data
            self.stack[top+3] = data


    def pop(self, stack_no):
        top = self.get_top(stack_no)
        if not self.is_empty(top):
            retval = self.stack[top]
            self.stack[top] = "-"
            return retval


    def peek(self, stack_no):
        top = self.get_top(stack_no)
        if not self.is_empty(top):
            return self.stack[top]


if __name__ == "__main__":
    s = Stack()
    print(s.stack)
    s.push(10,1)
    print(s.stack)
    s.push(8,3)
    print(s.stack)
    s.push(7,2)
    print(s.stack)
    s.push(7,2)
    print(s.stack)
    s.push(7,2)
    print(s.stack)
    s.push(7,2)
    print(s.stack)
    s.push(10,1)
    print(s.stack)
    s.push(12,1)
    print(s.stack)
    print(s.peek(1))
    print(s.peek(2))
    print(s.peek(3))
    print("popped", s.pop(1))
    print(s.stack)
    print("popped", s.pop(2))
    print(s.stack)
    print("popped", s.pop(3))
    print(s.stack)


    
    print("All good")

