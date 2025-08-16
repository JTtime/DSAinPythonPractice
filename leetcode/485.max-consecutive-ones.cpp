/*
 * @lc app=leetcode id=485 lang=cpp
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0;
        int count = 0;

        for (int num: nums) {
            if (num==1){
                count++;
            }
            if (num==0) {
                count=0;
            }
            maxCount=std::max(maxCount, count);
        }

        return maxCount;
    }
};
// @lc code=end

