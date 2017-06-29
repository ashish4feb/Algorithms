class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rec1 = [[A,B],[C,B],[C,D],[A,D]]
        rec2 = [[E,F],[G,F],[G,H],[E,H]]
        def overlaping(rec1,rec2):
            if rec1[0][0]>rec2[1][0] or rec1[1][0]<rec2[0][0]:
                return False
            if rec1[0][1]>rec2[2][1] or rec1[2][1]<rec2[0][1]:
                return False
            return True
        def area(rec):
            return (rec[1][0]-rec[0][0])*(rec[2][1]-rec[0][1])
            
        if overlaping(rec1,rec2):
            j=max(A,E)
            k=max(B,F)
            l=min(C,G)
            m=min(D,H)
            rec = [[j,k],[l,k],[l,m],[j,m]]
            return area(rec1) + area(rec2) - area(rec)
        else:
            return area(rec1)+area(rec2)
