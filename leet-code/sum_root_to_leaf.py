# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumberUtil(0,root)

    def sumNumberUtil(self,val,root):
        if root == None:
            return 0

        val = 10 * val + root.val
        if root.left == None and root.right == None:
            return val

        return self.sumNumberUtil(val,root.left) + self.sumNumberUtil(val,root.right)


tree = TreeNode(0)
tree.left = TreeNode(1)
sol = Solution()
print(sol.sumNumbers(tree))
