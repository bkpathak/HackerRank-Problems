class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def add_node_front(self,val):
        new_node = Node(val)
        
def segregate_even_odd(head):
