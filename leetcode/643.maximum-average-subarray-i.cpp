/*
 * @lc app=leetcode id=643 lang=cpp
 *
 * [643] Maximum Average Subarray I
 */

// @lc code=start
#include <algorithm>
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int l=0;
        int r=k-1;
        double maxAverage = -1e9;
        long long sum = 0;

        for (int i=0; i<k; i++) {
            sum+=nums[i];
        }

        long long maxSum = sum;

        for (int i=k; i<nums.size(); i++) {
            sum+=nums[i]-nums[i-k];
            maxSum= std::max(maxSum, sum);
        }

        return (double) maxSum/k;



//following commented code passed 124/127 cases but failed 3 cases for TLE
        // while (r<nums.size()) {
        //     // int sum = 0;
        //     for (int i=l; i<=r; i++) {
        //         sum+=nums[i];
        //     }
        //     double avg = (double)sum/k;
        //     maxAverage = std::max(maxAverage, avg);
        //     r++;
        //     l++;
        // }
        // return maxAverage;
        
    }
};
// @lc code=end

