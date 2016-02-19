'''

Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a- >b- >d->e

'''


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
        self.root = root
        self.size = 0 if not root else 1

    def add (self,data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
        

    def __str__(self):
        cur_node = self.root
        lst_string = ""
        while cur_node:
            lst_string += str(cur_node.data) 
            if cur_node.next:
                lst_string += " > "

            cur_node = cur_node.next

        return lst_string

    def delete_node(self, node):
        if node is None: return
        
        next_node = node.next
        if next_node is None: return

        #copy data from next node
        node.data = next_node.data
        #delete next node 
        node.next = next_node.next
        self.size -= 1

        



if __name__ == "__main__":

    #sized correctly
    l = LinkedList(Node(10))
    assert l.size == 1
    l.add(9)
    l.add(8)
    assert l.size == 3
    print(l)
    l.delete_node(l.root.next)
    print(l)
    assert l.size == 2
    l.delete_node(l.root)
    print(l)
    assert l.size == 1

        
