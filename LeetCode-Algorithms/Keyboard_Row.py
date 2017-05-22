class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        patt = re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$')
        return filter(patt.match,words)
