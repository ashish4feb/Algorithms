# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth = 0
        def trav(root):
            if root ==None:
                return 0
            lmax = trav(root.left)
            rmax = trav(root.right)
            root.val = lmax+rmax
            if root.val > self.maxDepth:
                self.maxDepth = root.val
            return max(lmax,rmax) +1
        trav(root)
        return self.maxDepth
