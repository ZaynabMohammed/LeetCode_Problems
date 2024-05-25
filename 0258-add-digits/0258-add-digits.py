class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))==1:
            return num
        else:
            x=0
            while ( len(str(num))!=1 ):
                num=sum(int(i) for i in str(num))  
            return num        
                
            
        