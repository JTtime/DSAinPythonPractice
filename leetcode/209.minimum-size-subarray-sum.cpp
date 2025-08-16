/*
 * @lc app=leetcode id=209 lang=cpp
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0;
        int leastCount = nums.size();
        int right = 0;
        int sum = 0;
        bool ansFound = false;

        while (right < nums.size()) {
            sum+=nums[right];

            while (sum>=target) {
                ansFound = true;
                leastCount=std::min(leastCount, right-left+1);
                sum-=nums[left];
                left++;                
            }
            right++;
        }

        return ansFound ? leastCount : 0;
    }
};
// @lc code=end

