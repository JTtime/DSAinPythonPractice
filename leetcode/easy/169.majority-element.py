#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       n = len(nums)

       #Moore's voting algorithm

       ans=nums[0]
       count=0

       for index, value in enumerate(nums):
           if (count==0):
               ans = value
            
           if (ans==value):
               count+=1
            
           if (ans!=value):
               count-=1
        
       count=0
       for index, value in enumerate(nums):
           if (ans==value):
               count+=1
            
        
       if (count>n/2):
           return ans
           
               
           


       #Brute force passes only 42 of 53 test cases
    #    for i, static_value in enumerate(nums):
    #        frequency=0
    #        for j, checking_value in enumerate(nums):
    #            if static_value==checking_value:
    #                frequency+=1
                
            
    #        if frequency>(n/2):
    #                return static_value
                   
               
        
# @lc code=end

