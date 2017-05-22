# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left == None:
            l_depth = 0
        else:
            l_depth = self.maxDepth(root.left)
        if root.right == None:
            r_depth = 0
        else:
            r_depth = self.maxDepth(root.right)
        return max(l_depth,r_depth) + 1
