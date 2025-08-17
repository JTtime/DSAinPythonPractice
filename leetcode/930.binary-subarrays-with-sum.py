#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count_array(nums: List[int], goal: int):
            left=0
            count=0
            sum=0
        
            for right, num in enumerate(nums):
                sum+=num
                while (left<=right and sum>goal ):
                    sum-=nums[left]
                    left+=1
                
                count+= (right - left + 1)
            
            return count
    
        return count_array(nums, goal) - count_array(nums, goal-1)
    
    
    
        
        
        
# @lc code=end

