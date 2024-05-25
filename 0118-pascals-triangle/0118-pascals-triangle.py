class Solution:
    def generate(self,numRows):
        my_list=[[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows,1):
            k=1
            while k <=i-1:
                my_list[i][k]=my_list[i-1][k-1]+my_list[i-1][k]
                k=k+1
        return my_list