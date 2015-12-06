class SkipNode(Object):
    """
    The node contains elements and pointer to the next node for all the level
    where the element is present.
    """
    def __init__(slef, val = None, level = 0):
        self.val = val
        self.next = [None] * level

class SkipList(Object):
    def __init__(self):
        self.head = SkipNode()
        self.count = 0
        self.height = 0

    def choose_random_height(max_level):
        """
        Choose the maximum level for the node. Here "fixed dice" approach is used
        which will restrict the maximum height of the new node to the current max_level
        of the SkipList + 1.
        """
        level = 1
        prob = 0.5
        while(random() < prob and level < max_level):
            level += 1

        return level
