/*
 * @lc app=leetcode id=229 lang=cpp
 *
 * [229] Majority Element II
 */

// @lc code=start
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int count_one=0;
        int count_two=0;
        int n = nums.size();
        int candidate1=-1;
        int candidate2=-1;
        // std::vector<int> ans(2);
        std::vector<int> result;

        for (int i=0; i<n; i++) {
            if (count_one==0 && candidate2!=nums[i]) {
                candidate1=nums[i];
                count_one=1;
            } else if (count_two==0 && candidate1!=nums[i]) {
                candidate2=nums[i];
                count_two=1;
            } else if (candidate1==nums[i]) {
                count_one++;
            } else if (candidate2==nums[i]) {
                count_two++;
            } else {
                count_one--;
                count_two--;
            }
        }

        int count_a=0;
        int count_b=0;

        for (int i = 0; i<n; i++) {
            if (candidate1==nums[i]) {
                count_a++;
            } else if (candidate2==nums[i]) {
                count_b++;
            }
        }

        if (count_a>n/3) {
            result.push_back(candidate1);
        }
        if (count_b>n/3) {
            result.push_back(candidate2);
        }

        return result;

        
        
    }
};
// @lc code=end

