#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                up = dp[i-1][j] if i > 0 and dp[i-1][j]!=-1 else 0
                left = dp[i][j-1] if j > 0 and dp[i][j-1]!=-1 else 0
                dp[i][j] = up + left
        return dp[m-1][n-1]

        # def dfs(m, n):
        #     if obstacleGrid[m][n]==1:
        #         dp[m][n]=0
        #         return 0
        #     if m==0 and n==0:
        #         dp[0][0] = 1
        #         return 1
        #     if m<0 or n<0:
        #         return 0
            
            # if dp[m][n]!=-1:
            #     return dp[m][n]
        #     up = dfs(m-1, n)
        #     left = dfs(m, n-1)
        #     dp[m][n] = up + left
        #     return up + left
        # return dfs(m-1, n-1)        
# @lc code=end

