/*
 * @lc app=leetcode id=746 lang=cpp
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        vector<int> dp(n+2, -1);
        dp[0] = 0;
        dp[1] = 0;
        for (int i=2; i<=n; i++) {
            dp[i] = std::min((cost[i-1] + dp[i-1]), (cost[i-2] + dp[i-2]));
        }
        return dp[n];
    }
};
// @lc code=end

