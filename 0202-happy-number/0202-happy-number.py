class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (len(str(sum(int(i)**2 for i in str(n)))) == 1):
            v=str(sum(int(i)**2 for i in str(n)))
        else:
            v=str(n)

        if len(v)==1:
            v=str(sum(int(i)**2 for i in v))
            while len(v) != 1:
                v=str(sum(int(i)**2 for i in v))  
        else:    
            while len(v) != 1:
                v=str(sum(int(i)**2 for i in v))

        if v=='1':
            return True
        else:
            return False   
        