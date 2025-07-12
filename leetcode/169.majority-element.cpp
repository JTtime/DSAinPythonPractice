/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count=0;
        int n = nums.size();
        int element = nums[0];
        for (int i=0; i<n; i++) {
            if (count==0) {
                element=nums[i];
            }
            if (element==nums[i]) {
                count++;
            }
            if (element!=nums[i]) {
                count--;
            }
        }

        count=0;

        for (int i=0; i<n; i++) {
            if (element==nums[i]) {
                count++;
            }
        }

        if (count > n/2) {
            return element;
        }

        return -1;
        
    }
};
// @lc code=end

