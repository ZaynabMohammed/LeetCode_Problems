class Solution:
    def num_of_digits(self, nums) :
        count=[n for n in nums if n%2==0 ]
        return(len(count))
    def findNumbers(self,nums):
       new_list = [len(str(n)) for n in nums ]
       return self.num_of_digits(new_list)
    