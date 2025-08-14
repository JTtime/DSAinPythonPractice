/*
 * @lc app=leetcode id=1343 lang=cpp
 *
 * [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
 */

// @lc code=start
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int count=0;
        int sum=0;
        for (int i=0; i<k; i++) {
            sum+=arr[i];
        }
        if ((sum/k)>=threshold) {
                count++;
            }

        for (int i=k; i<arr.size(); i++) {
            sum+=arr[i]-arr[i-k];
            if ((sum/k)>=threshold) {
                count++;
            }
        }

        return count;
        
    }
};
// @lc code=end

