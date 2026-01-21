#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        x=len(matrix)
        dp=[[float('inf') for _ in range(x)] for _ in range(x)]

        for k, v in enumerate(matrix[x-1]):
            dp[x-1][k] = v
        
        for i in range(x-1, -1, -1):
            for j in range(x-1, -1, -1):
                if i==x-1:
                    continue
                down = dp[i+1][j]
                diag_left = diag_right = float('inf')
                if j>0:
                    diag_left = dp[i+1][j-1]
                if j<(x-1):
                    diag_right = dp[i+1][j+1]
                dp[i][j] = min(down, diag_left, diag_right) + matrix[i][j]
        return min(dp[0][j] for j in range(x))




        # def dfs(m,n):
        #     if m==x-1:
        #         dp[m][n]=matrix[m][n]
        #         return matrix[m][n]
        #     if dp[m][n]!=float('inf'):
        #         return dp[m][n]
        #     down=dfs(m+1, n)
        #     diag_left = diag_right = float('inf')
        #     if n>0:
        #         diag_left=dfs(m+1, n-1)
            
        #     if n<(x-1):
        #         diag_right=dfs(m+1, n+1)
        #     dp[m][n] = min(down, diag_left, diag_right) + matrix[m][n]
        #     return dp[m][n]
        # return min(dfs(0, j) for j in range(x))
# @lc code=end

