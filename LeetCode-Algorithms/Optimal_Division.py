class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        series = map(str,nums)
        if len(nums) <= 2:
            return '/'.join(series)
        return series[0]+'/('+'/'.join(series[1::])+')'
