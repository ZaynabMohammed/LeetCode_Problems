class Solution:
    def sumOddLengthSubarrays(self, arr):
        x=sum(arr)
        L=len(arr)
        if L % 2 != 0 and L!= 1:
            x+=x
        else:
            L+=1
        for n in range(L-2,2,-2):
            for i in range(0,len(arr)):
                if i+n == len(arr):
                    x+= sum(arr[i:i+n])
                    break;
                else:
                    x+= sum(arr[i:i+n])
        return x