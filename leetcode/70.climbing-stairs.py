#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #dp memoization approach
        # if n<=2:
        #     return n
        # dp = [-1]*(n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2
        
        # def helper(n, dp):
        #     if n<=2:
        #         return n
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = helper(n-1, dp) + helper(n-2, dp)
        #     return dp[n]    
        
        # return helper(n, dp)
        
        
        #dp tabulation approach
        # if n<=2:
        #         return n
        # def helper(n, dp):
            
            
        #     for i in range(3, n+1):
        #         dp[i] = dp[i-1] + dp[i-2]
                
        #     return dp[n]
        
        # dp=[0]*(n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2
        
        # return helper(n, dp)        
        
# @lc code=end

