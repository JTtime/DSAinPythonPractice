/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, j = 1, k = 1;

        while (j<nums.size()) {
            if (nums[j]==nums[j-1]) {
                j++;
            } else {
                nums[i+1] = nums[j];
                j++;
                i++;
                k++;
            }
        }

        return k;
    }
};
// @lc code=end

