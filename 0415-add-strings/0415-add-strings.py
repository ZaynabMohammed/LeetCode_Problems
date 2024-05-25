class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if (len(num1)>len(num2)):
            num2=num2.zfill(len(num1))
        elif (len(num1)<len(num2)): 
            num1=num1.zfill(len(num2)) 
        rem=0
        res=''
   

        for i in range (len(num1)-1,-1,-1):
            summ=0
            summ+= int(num1[i])+int(num2[i])+rem
            if summ >=10 and i!=0:
                rem = 1
                res+=str(summ)[1]
            elif  summ >=10 and i==0:
                 res+=str(summ)[::-1]
                 print(res)  
            else:
                res+=str(summ)
                rem=0
                continue
        return res[::-1]            