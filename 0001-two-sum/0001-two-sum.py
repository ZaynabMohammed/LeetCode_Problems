class Solution(object):
    def twoSum(self, nums, target):
        # l=[]
        # for i,x in enumerate(nums):
        #     for j in range(i+1,len(nums)):
        #         if (x + nums[j])== target :
        #             l.append(i)
        #             l.append(j)
        # return l
        myList=[[i,j] for i,x in enumerate(nums) for j in range(i+1,len(nums)) if (x + nums[j])== target]
        return myList[0]