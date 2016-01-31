# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
For binary tree we have at max 2 child. So we calculated the diameter
of its left subtree and right subtree and then looked for max of these
values.
 Now in n-ary tree as we have at max n child nodes so we have to
 calculate the Diameter of each subtree rooted by the n child nodes,
 then get the max value out of these n diameters. Suppose this value
 is maxChildDiameter. Now we need to calculate the value of diameter
 through the current node.(this is corresponding to the 3rd value for
 binary tree) For calculating it we need to calculate the 2 nodes which
 are at maximum distance from the current node and these 2 should be in
 different child subtrees. For finding them we need to iterate over all
 the child nodes and for each of them we need to find the maximum distant
 node and need to calculate the maximum distance. After completion of
 iteration over all child nodes we need to find max value out of them
 and second max value. We will add these 2 values + the distances to
 their corresponding root node to our current node. This value will
 become the Diameter through the current Node. Now we need to compare
 this value with the maxChildDiameter value. The greater of these two
 values will become the Diameter of subtree rooted at the current Node.
"""
class Dist_Diameter(object):
    def __init__(self):
        self.diameter=0
        self.max_distance=0


class Node(object):
    def __init__(self,weight = 0,children =[]):
        """
        The children are represented as list.
        """
        self.weight = weight
        self.children = children

def tree_diameter(tree):
    ret = Dist_Diameter()
    if tree == None or tree == []:
        ret.diameter = 0
        ret.max_distance = 0
        return ret

    max_diameter = 0
    max_child_diameter = 0
    sec_max_child_diameter = 0

    print(tree.children)
    for child in tree.children:
        d = tree_diameter(child.children)

        if d.max_distance > max_child_diameter:
            sec_max_child_diameter = max_child_diameter
            max_child_diameter = d.max_distance
        elif d.max_distance > sec_max_child_diameter:
            sec_max_child_diameter = d.max_distance
        max_diameter = max(d.diameter,max_diameter)

    ret.diameter = max(max_diameter, max_child_diameter+ sec_max_child_diameter)
    ret.max_distance = max_diameter + tree.weight
    return ret


# Tree is represneted recursively
tree1 = Node(0)
tree2 = Node(0,[Node(5)])
tree3 = Node(0,[Node(5,[Node(4,[Node(7)])])])
tree4 = Node(0,[Node(5,[Node(8,[Node(7)])])])
tree5 = Node(0,[
             Node(1,[Node(5),Node(7)]),
             Node(1,[Node(5),Node(6)]),
             Node(1,[Node(9),Node(10)])
             ])
tree6 = Node(0,[
             Node(5,[Node(8),Node(7)]),
             Node(5,[Node(9),Node(8)]),
             Node(5,[Node(10),Node(9)])
             ])
data = [tree1,tree2,tree3,tree4,tree5]

for d in data:
    print(tree_diameter(d).diameter)
