/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+2, -1);
        dp[n] = 1;
        dp[n+1] = 0;
        for (int i=n-1; i>=0; i--) {           

            dp[i] = dp[i+1] + dp[i+2];
        }
        return dp[0];
    }

    // int count (int i, int n, vector<int> dp) {
    //     if (i==n) {
    //         return  1;
    //     }
    //     if (i>n) {
    //         return 0;
    //     }

    //     return count(i+1, n, dp) + count(i+2, n, dp);
    // }
};
// @lc code=end

