class Solution(object):
    def climbStairs(self, n):
        a=1
        b=2
        if n==1:
            return a
        elif n==2:
            return b
        else:  
            for i in range(2, n):
                c = a + b
                a = b
                b = c
            return b