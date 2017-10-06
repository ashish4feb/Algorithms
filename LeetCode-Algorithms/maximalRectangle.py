class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        mArea = 0
        level = [0 for i in range(len(matrix[0]))]
        def area(lvl):
            stack = [-1]
            lvl.append(0)
            ar = 0
            for i in range(len(lvl)):
                while len(stack)!=0 and lvl[stack[-1]]>=lvl[i]:
                    top = stack.pop(-1)
                    h = lvl[top]
                    if len(stack)!=0:
                        off = stack[-1]
                    else:
                        off = 0
                    ar = max(ar,h*(i-off-1))
                stack.append(i)
            return ar
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='1':
                    level[j]+=1
                else:
                    level[j]=0
            mArea = max(mArea,area(level))
        return mArea
