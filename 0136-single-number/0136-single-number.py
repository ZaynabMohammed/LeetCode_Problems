class Solution:
    def singleNumber(self, nums):
        for n in nums:
            if nums.count(n)==1:
                return n
        
       # return n  for n in nums if nums.count(n)==1
        