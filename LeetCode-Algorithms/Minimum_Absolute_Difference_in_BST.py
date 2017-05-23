# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        first = -sys.maxint-1
        sec = 0
        m_diff = sys.maxint
        stack = []
        stack.append(root)
        head = root.left
        #sec = root.val
        while len(stack)!=0 or head!=None:
            if head!=None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                sec = head.val
                head = head.right
                diff = sec - first
                m_diff = min(diff,m_diff)
                first = sec
        return m_diff
