#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right=0
        leastCount = len(nums)
        sum=0
        ansFound=False

        while right<len(nums):
            sum+=nums[right]

            while sum>=target:
                ansFound=True
                leastCount = min(leastCount, right-left+1)
                sum-=nums[left]
                left+=1
                
                
            
            right+=1
        
        return leastCount if ansFound else 0
        
# @lc code=end

