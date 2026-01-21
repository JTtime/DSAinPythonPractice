#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target = sum(nums)
        if target%2==1:
            return False
        t = target//2
        dp = [[-1 for _ in range(t+1)] for _ in range(n+1)]
        
        
        for i in range(n+1):
            dp[i][0] = True
        
        for j in range(1, t+1):
            dp[n][j] = False
        
        for i in range(n-1, -1, -1):
            for j in range(1, t+1):
                pick = False
                if j>=nums[i]:
                    pick = dp[i+1][j-nums[i]]
                not_pick = dp[i+1][j]
                dp[i][j] = pick or not_pick
        
        return dp[0][t]
# @lc code=end

