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

    def find_kth_to_last(self,kth):
        '''find kth to last element
        since my linked list stored the size it's trivial'''
        if kth >= self.size: return None 

        idx = self.size - kth
        node = self.root
        for i in range(idx-1):
            node = node.next

        return node


    def compute_size(self):
        node = self.root
        if not node: return 0

        i = 0
        while node:
            i+=1
            node = node.next

        return i

        
    def find_jth_to_last(self, jth):
        ''' find jth to last element assuming
        we don't know the lenght of the list
        by computing the lenght of the list
        then doing the standard find'''
        
        self.size = self.compute_size()
        return self.find_kth_to_last(jth)

    def find_ith_to_last(self, ith):
        '''let's find it without knowing the lenght of the
        list plus trying to keep to one loop of the list'''
    
        node = self.root
        if not node: return None

        #move node forward by ith places
        for i in range(ith):
            try:
                node = node.next
            except AttributeError:
                #ith is to large
                return None


        follow_node = self.root 
        #last element should be ith = 0
        node = node.next

        while node:
            follow_node = follow_node.next
            node = node.next

        return follow_node
    
    def find_nth_to_last(self, head, nth):
        self.iiter = -1
        return self.find_nth_to_last_rec(head, nth)

    def find_nth_to_last_rec(self, head, nth):
        '''recursive style'''
        if head is None: return None

        node = self.find_nth_to_last_rec(head.next, nth)

        self.iiter += 1
        if self.iiter == nth:
            return head

        return node

        

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
    l = LinkedList(Node(10))
    assert l.size == 1
    l.add(9)
    l.add(8)
    l.add(7)
    l.add(6)
    l.add(5)
    l.add(4)
    l.add(3)
    l.add(2)
    l.add(1)
    print(l)
    assert l.find_kth_to_last(0).data == 10
    assert l.find_kth_to_last(9).data == 1
    assert l.find_kth_to_last(5).data == 5 
    assert l.find_kth_to_last(12) == None 

    assert l.find_jth_to_last(0).data == 10
    assert l.find_jth_to_last(9).data == 1
    assert l.find_jth_to_last(5).data == 5 
    assert l.find_jth_to_last(12) == None 

    assert l.find_ith_to_last(0).data == 10
    print l.find_ith_to_last(9).data
    assert l.find_ith_to_last(9).data == 1
    assert l.find_ith_to_last(5).data == 5 
    assert l.find_ith_to_last(12) == None 

    #assert l.find_nth_to_last(l.root, 0).data == 10
    assert l.find_nth_to_last(l.root, 9).data == 1
    #assert l.find_nth_to_last(l.root, 5).data == 5 
    #assert l.find_nth_to_last(l.root, 12) == None 

        
