/*
 * @lc app=leetcode id=930 lang=cpp
 *
 * [930] Binary Subarrays With Sum
 */

// @lc code=start
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return count(nums, goal) - count(nums, goal-1);        
    }
    int count(vector<int>& nums, int goal) {
        int left = 0;
        int array_count=0;
        int sum=0;

        for (int right = 0; right<nums.size(); right++) {
            sum+=nums[right];
           
            while (left<=right && sum>goal) {
                sum-=nums[left];
                left++;
            }
            array_count += (right - left + 1);
        }

      
        return array_count;
    }
};
// @lc code=end

