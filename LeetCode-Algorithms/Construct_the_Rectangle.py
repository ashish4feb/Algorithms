class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area==0:
            return [0,0]
        x = int(math.sqrt(area))
        while area % x != 0:
            x -=1
        return [area/x,x]
