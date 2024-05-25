class Solution:
    def findMaxConsecutiveOnes(self,nums):
        list1=[]
        list2 = []
        if (0 not in nums):
            return nums.count(1)
        else:
         list1= [i for i, x in enumerate(nums) if x == 0]
         list2.append(list1[0])
         if len(list1)==1:
          k=len(nums)-1-list1[0]
          if  k>list1[0]:
            return k
          else:
                return list1[0]
         else:
             if nums[len(list1)-1] !=0:
                 list2.append(len(nums) - 1 - list1[len(list1)-1])
             for i in range (1,len(list1),1):
              list2.append(list1[i]-list1[i-1]-1)
             return max(list2)