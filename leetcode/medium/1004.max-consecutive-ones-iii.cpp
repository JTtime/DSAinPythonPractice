/*
 * @lc app=leetcode id=1004 lang=cpp
 *
 * [1004] Max Consecutive Ones III
 */

// @lc code=start
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int max_count=0;
        int zero_count=0;
        int left = 0;

        for (int right = 0; right<nums.size(); right++) {
            if (nums[right]==0) {
                zero_count++;
            }
            while (zero_count>k) {
                if (nums[left]==0) {
                    zero_count-=1;
                }
                left++;
            }
            max_count=std::max(max_count, right-left+1);
        }

        return max_count;
        
    }
};
// @lc code=end

