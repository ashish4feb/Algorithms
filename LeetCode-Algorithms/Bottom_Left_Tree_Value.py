# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dep = {}
        self.dep[0] = root.val
        self.max_h = 0
        def trav(root,height):
            if root==None:
                return
            if root.left==None and root.right==None:
                if height > self.max_h and height not in self.dep:
                    self.dep[height] = root.val
                    self.max_h = height
            trav(root.left,height+1)
            trav(root.right,height+1)
        trav(root,0)
        return self.dep[self.max_h]
