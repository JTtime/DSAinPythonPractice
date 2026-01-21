#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x = len(grid) - 1
        y=len(grid[0]) - 1
        dp=[[-1 for _ in range(y+1)] for _ in range(x+1)]

        dp[x][y] = grid[x][y]

        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if i==x and j==y:
                    continue
                down = dp[i+1][j] if i< x else float('inf')
                right = dp[i][j+1] if j<y else float('inf')
                dp[i][j] = min(down,  right) + grid[i][j]
        return dp[0][0]
# @lc code=end

