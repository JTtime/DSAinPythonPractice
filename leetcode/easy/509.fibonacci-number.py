#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # recursive approach
        # if n<=1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        
        #dp top down approach        
        
        # dp = [-1]*(n+1)        
        
        # def helper(n, dp):
        #     if n<=1:
        #         return n
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = helper(n-1, dp) + helper(n-2, dp)
        #     return dp[n]
        
        # return helper(n, dp)       
        
        
        #dp bottom up approach
        # dp = [-1]*(n+1)
        # if n<=1:
        #     return n
        # dp[0] = 0
        # dp[1] = 1      
        
        
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]        
        # return dp[n]
        
        
        
            
        
# @lc code=end

