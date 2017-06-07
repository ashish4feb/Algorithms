class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        op = {'(':')','{':'}','[':']'}
        for each in s:
            if each in op:
                stack.append(each)
            else:
                if len(stack)!=0:
                    popped = stack.pop()
                    if each != op[popped]:
                        return False
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
