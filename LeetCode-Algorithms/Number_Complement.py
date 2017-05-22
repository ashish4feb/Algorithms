class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = "{0:b}".format(num)
        z = num^(2**len(str(x))-1)
        return z
