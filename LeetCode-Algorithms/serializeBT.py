class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder)==0 or (len(preorder)>1 and preorder[0]=='#'):
            return False
        nHash = 1
        flag = 0
        string = preorder.split(',')
        for each in string:
            flag +=1
            if each == '#':
                nHash -= 1
            else:
                nHash +=1
            if nHash <= 0:
                break
        #print(flag,nHash,len(preorder))
        if nHash ==0 and flag == len(string):
            return True
        else:
            return False
