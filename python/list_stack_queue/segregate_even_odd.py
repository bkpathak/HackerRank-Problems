class Node(object):
    """
    Creates the Node
    """
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def add_node_front(self,val):
        """
        Adds the lsit at the front of the List
        """
        self.count += 1
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def segregate_even_odd(self):
        """
        Segreagte the List in even and odd; even first and then odd.
        """
        tail = self.head
        prev = Node(None) # Dummy Node
        curr = self.head
        n = self.count

        while tail.next is not None:
            tail = tail.next
        set_head = False
        while n > 0 :
            if curr.val % 2 == 1:
                # break the link between even and odd node
                prev.next = curr.next
                # Move the current node to the end
                curr.next = None
                tail.next = curr
                tail = curr
                curr = prev.next

            else:
                if not set_head:
                    self.head = curr
                    set_head = True
                prev = curr
                curr = curr.next
            n -= 1

    def list_traverse(self):
            temp = self.head
            while temp is not None:
                print(temp.val, end = " ")
                temp = temp.next

if __name__ == "__main__":
    data = [1,7,3,4,1,2,6,4,19,8,2,4,5]
    llist = LinkList()

    for d in data:
        llist.add_node_front(d)

    print("Before Segregation:")
    llist.list_traverse()

    # Segregate the List
    llist.segregate_even_odd()
    print()
    print("After Segregation:")
    llist.list_traverse()
    print()
