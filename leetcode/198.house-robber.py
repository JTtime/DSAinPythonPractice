#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        dp=[0]*(n+1)
        
        
        if n==0:
            return nums[0]
        if n==1:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        #2,7,9,3,1
        for i in range(2, n+1):
            pick = nums[i] + dp[i-2]
            npick = dp[i-1]
            dp[i] = max(pick, npick)
        
        return dp[n]
            
        
# @lc code=end

