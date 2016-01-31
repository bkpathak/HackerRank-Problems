import random as rn
class SkipNode(object):
    """
    The node contains valueents and pointer to the next node for all the level
    where the valueent is present.
    """
    def __init__(self, val = None, level = 0):
        self.val = val
        self.next = [None] * level

class SkipList(object):
    def __init__(self):
        self.head = SkipNode()
        self.count = 0
        self.height = 0

    def __choose_random_height(self):
        """
        Choose the maximum level for the node. Here "fixed dice" approach is used
        which will restrict the maximum height of the new node to the current max_level
        of the SkipList + 1.
        """
        level = 1
        prob = 0.5
        while(rn.random() < prob):
            level += 1
            if level == self.height:
                return self.height + 1

        return level

    def search_value(self,value):
        """
        Search the valueent in SkipList. If fouinds returns True else False.
        The implementation is straight forward. Start from the head valueents top
        most reference.Check the top most reference e,  is less then , equals to
        or grater then the valueent we are looking for. If greater than then the
        value exists at right, if less then the value exists at left otherwise we
        found the value.
        """
        current = self.head
        for i in reversed(range(self.height)):
            while current.next[i] is not None and current.next[i].val <= value:
                if current.next[i].val == value:
                    return True
                current = current.next[i]
        return False


    def insert_value(self,value):
        """
        Determine the level of the new nodes. Starting from the top reference of the
        head node, update each level which is less then or equals to the height of the
        new node.
        """
        level = self.__choose_random_height()

        # Create the new node
        new_node = SkipNode(value,level)
        # Update the height of the SkipList
        self.height = max(self.height,level)
        self.count += 1

        while len(self.head.next) < len(new_node.next):
            self.head.next.append(None)

        current = self.head
        for i in reversed(range(self.height)):
            while current.next[i] is not None and current.next[i].val < value:
                if current.next[i].val >  value:
                    break
                current = current.next[i]

            # insert the new node

            if i < level:
                new_node.next[i] = current.next[i]
                current.next[i] = new_node

    def remove_node(self, value):
        """
        If found remove the node from every level including the base level
        """
        current = self.head

        for i in reversed(range(self.height)):
            while current.next[i] is not None and current.next[i].val <= value:
                if current.next[i].val == value:
                    current.next[i]=current.next[i].next[i]
                    self.count -= 1
                    if self.head.next[i] is None:
                        self.height -= 1
                    break
                current = current.next[i]

    def skip_list_enumerate(self):
        """
        Enumerate over the skip list.
        """
        current = self.head.next[0]
        while current is not None:
            yield current.val
            current = current.next[0]

skip_list = SkipList()
## add element to the skip list
skip_list.insert_value(10)
skip_list.insert_value(5)
skip_list.insert_value(15)
skip_list.insert_value(13)

## print element of the skip list
for node in skip_list.skip_list_enumerate():
    print(node)

## check element present in the skip list
print("Check 10 is presnt in the skip list or not.")
if skip_list.search_value(10):
    print("Value presnt in the list.")
else:
    print("Value not present in list.")

## Remove element from the skip list
skip_list.remove_node(10)

## check element present in the skip list
print("Check 10 is presnt in the skip list or not after removal.")
if skip_list.search_value(10):
    print("Value presnt in the list.")
else:
    print("Value not present in list.")

## print element of the skip list after removal
for node in skip_list.skip_list_enumerate():
    print(node)
