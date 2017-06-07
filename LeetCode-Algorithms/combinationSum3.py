class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        def comb(res,tar,nums,k):
            if k==1:
                if tar in nums:
                    self.res.append(res[:]+[tar])
            else:
                for i in range(len(nums)):
                    res.append(nums[i])
                    #print(res)
                    comb(res,tar-nums[i],nums[i+1:],k-1)
                    res.pop()
        nums = [i for i in range(1,10)]
        res =[]
        comb(res,n,nums,k)
        return self.res
