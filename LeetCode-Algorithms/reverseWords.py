class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sen = s.split(" ")
        return ' '.join(word[::-1] for word in sen)
