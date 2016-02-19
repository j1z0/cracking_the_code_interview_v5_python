'''simple linked list'''

class Node(object):
    '''
    The individual pieces of a linked list are the
    Nodes
    '''
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, root = None):
        self.root = Node(root)
        self.size = 0 if not root else 1

    def add (self,data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def delete(self, data):
        cur_node = self.root
        prev_node = None
        while cur_node:
            if cur_node.data == data:
                if prev_node :
                    prev_node.next = cur_node.next
                else:
                    self.root = cur_node.next
                self.size -= 1
                return True
            else: # didn't find
                prev_node = cur_node
                cur_node = cur_node.next
        return False # not found


    def find(self, d):
        cur_node = self.root
        while cur_node:
            if cur_node.data == d:
                return cur_node
            else:
                cur_node = cur_node.next

        return None



if __name__ == "__main__":

    print("running tests")
    #sized correctly
    l = LinkedList()
    assert l.size == 0

    l = LinkedList(23)
    assert l.size == 1

    #add
    l.add(58)
    assert l.size == 2
    assert l.root.data == 58
    assert l.root.next.data == 23
    assert l.root.next.next == None


    #delete from middle
    l.add(100)
    assert l.size == 3
    l.delete(58)
    assert l.size == 2
    assert l.root.data == 100
    assert l.root.next.data == 23
    assert l.root.next.next == None

    #delete first
    l.add(583)
    assert l.size == 3
    l.delete(583)
    assert l.size == 2
    assert l.root.data == 100 
    assert l.root.next.data == 23
    assert l.root.next.next == None

    #find
    found = l.find(100)
    assert found == l.root
    assert found.next.data == 23

    found = l.find(23)
    assert found.data == 23
    assert found.next == None

    print("All good")
