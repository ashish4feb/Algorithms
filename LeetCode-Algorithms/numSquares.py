class Solution(object):
    dp = []
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<len(self.dp):
            dp = self.dp
        else:
            dp = self.dp + [each for each in range(len(self.dp),n+1)]
            for i in range(len(self.dp),n+1):
                root = int(math.floor(math.sqrt(i)))
                if root*root == i:
                    dp[i]=1
                else:
                    while root!=0:
                        dp[i] = min(dp[i],dp[i-root*root]+dp[root*root])
                        root -=1
            self.dp = dp
        return dp[n]
