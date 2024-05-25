class Solution(object):
    def isPalindrome(self, x):
        z=str(x)
        if (len(z) % 2 == 0):
            for i in range(0,len(z)//2):
                if( z[i]== z[len(z)-(i+1)] ):
                    continue
                else:
                    return False
            return True    
        elif z[0]=='-':
            return False
        else:
            j=len(z) // 2
            for i in range(1,j+1):
                if z[j-i]== z[j+i]:
                    continue
                else:
                    return False
            return True    
