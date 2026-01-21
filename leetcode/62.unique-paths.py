#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        dp[m-1][n-1]=1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j == n-1:
                    continue
                down = dp[i+1][j] if i+1<m else 0
                right = dp[i][j+1] if j+1<n else 0
                dp[i][j] = down + right
        

        return dp[0][0]

        

        # def dfs(x, y):
        #     if x==m-1 and y==n-1:
        #         dp[x][y]=1
        #         return 1
        #     if x>=m or y>=n:
        #         return 0
        #     if dp[x][y]!=-1:
        #         return dp[x][y]
        #     down=dfs(x+1, y)
        #     right=dfs(x, y+1)
        #     dp[x][y] = down+right

        #     return down+right
        # return dfs(0, 0)
        #     if m==0 and n==0:
        #         dp[0][0] = 1
        #         return 1
        #     if m<0 or n<0:
        #         return 0
        #     if dp[m][n]!=-1:
        #         return dp[m][n]
        #     up = dfs(m-1, n)
        #     left = dfs(m, n-1)
        #     dp[m][n] = up + left
        #     return up + left
        # return dfs(m-1, n-1)
            

        # if m==1 and n==1:
        #     dp[0][0]=1
        #     return 1
        # if m<=0 or n<=0:
        #     return 0
        # if dp[m-1][n-1]!=-1:
        #     return dp[m-1][n-1]
        # up = self.uniquePaths(m-1, n)
        # left = self.uniquePaths(m, n-1)
        # dp[m-1][n-1] = up + left
        # return up + left    
# @lc code=end

