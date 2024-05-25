class Solution(object):
    def majorityElement(self, nums):
        coun=0
        x=0
        # print(l)
        for i in set(nums):
            if nums.count(i)>coun:
                coun= nums.count(i)
                x=i
        return x
        