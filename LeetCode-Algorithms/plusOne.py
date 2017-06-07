class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        res = []
        for i in range(len(digits)-1,-1,-1):
            ad = (digits[i]+carry)
            res.insert(0,ad%10)
            carry = ad//10
        if carry!=0:
            res.insert(0,carry)
        return res
