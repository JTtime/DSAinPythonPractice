/*
 * @lc app=leetcode id=2824 lang=cpp
 *
 * [2824] Count Pairs Whose Sum is Less than Target
 */

// @lc code=start
class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        sort(nums.begin(), nums.end());

        int count  = 0;
        while (i<j) {
            if ((nums[i] + nums[j]) < target) {
                count += j - i;
                i++;
            } else {
                j--;
            }
         }

         return count;
        
    }
};
// @lc code=end

