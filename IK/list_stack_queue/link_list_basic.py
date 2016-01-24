# Basic Link List Implementation

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def add_node_front(self,val):
        """
        Add node at the front of the lsit.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def add_node_end(self,val):
        """
        Add node at the end of the list
        """
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        new_node = Node(val)
        temp.next = new_node

    def add_after_nth(self,val,n):
        """
        Add node at the nth position
        """
        temp = self.head
        pos = 1
        while temp is not None:
            if n == pos:
                new_node = Node(val)
                new_node.next = temp.next
                temp.next = new_node
                break
            pos += 1
            temp = temp.next

    def reverse_list(self):
        """
        Reverse the linked list
        """
        current = self.head
        previous = None
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def reverse_list_recur(self):
        self.__reverse_list_recur_util(self.head)

    def __reverse_list_recur_util(self,temp):
        if temp.next is None:
            self.head = temp
            return
        self.__reverse_list_recur_util(temp.next)
        next_node = temp.next
        next_node.next = temp
        temp.next = None

    def list_traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end = " ")
            temp = temp.next
        print()

if __name__ == "__main__":
    link_list = LinkList()
    link_list.add_node_front(1)
    link_list.add_node_front(2)
    link_list.add_node_front(3)
    link_list.add_node_end(4)
    link_list.add_node_end(5)
    link_list.add_node_end(6)
    link_list.add_after_nth(100,6)
    link_list.list_traverse()
    link_list.reverse_list()
    link_list.list_traverse()
    link_list.reverse_list_recur()
    link_list.list_traverse()
