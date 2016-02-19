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

    def dedup(self):
        data = {} 
        cur_node = self.root
        prev_node = None
        while cur_node:
            if data.get(cur_node.data):
                #cut cur_node out of list
                prev_node.next = cur_node.next
            else:
                data[cur_node.data] = True
                prev_node = cur_node

            cur_node = cur_node.next
            

    def dedup_no_buffer(self, start_node=None):
        '''recursive'''
     
        if not start_node:
            start_node = self.root

        data = start_node.data
        cur_node = start_node.next
        prev_node = start_node

        while cur_node:
            if cur_node.data == data:
               prev_node.next = cur_node.next
            else:
                prev_node = cur_node

            cur_node = cur_node.next


        if start_node.next:
           self.dedup_no_buffer(start_node.next)


            
            


    def __str__(self):
        cur_node = self.root
        lst_string = ""
        while cur_node:
            lst_string += str(cur_node.data) 
            if cur_node.next:
                lst_string += " > "

            cur_node = cur_node.next


        return lst_string




if __name__ == "__main__":

    #sized correctly
    l = LinkedList(Node(23))
    assert l.size == 1
    l.add(10)
    l.add(15)
    l.add(15)
    l.add(10)
    l.add(12)
    l.add(12)
    l.add(12)
    l.add(12)
    l.add(12)
    print(l)
    l.dedup()
    print(l)
    l.add(10)
    l.add(15)
    l.add(15)
    l.add(10)
    l.add(12)
    l.add(12)
    l.add(12)
    l.add(12)
    l.add(12)
    print(l)
    l.dedup_no_buffer()
    print(l)

