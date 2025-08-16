#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxCount = 0
        left = 0
        zero_count=0
        
        for right, num in enumerate(nums):
            # if (num==1):
            #     count+=1
            #     right+=1
            if (num==0):
                zero_count+=1
                
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
                
            
            maxCount=max(maxCount, right-left+1)
        
        return maxCount
                    
                
        
# @lc code=end

