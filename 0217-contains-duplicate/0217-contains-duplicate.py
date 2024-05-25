class Solution(object):
    def containsDuplicate(self, nums):
        l=set(nums)
        if len(l) == len(nums):
            return False
        else:
            return True 