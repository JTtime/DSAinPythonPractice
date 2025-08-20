/*
 * @lc app=leetcode id=560 lang=cpp
 *
 * [560] Subarray Sum Equals K
 */

// @lc code=start
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
         int count = 0;
        int n = nums.size();

        vector<int> prefixArray(n, 0);
        prefixArray[0] = nums[0];

        for (int i=1; i<nums.size(); i++) {
            prefixArray[i] = nums[i] + prefixArray[i-1];
        }

        unordered_map<int, int> prefixMap;

        for (int j=0; j<nums.size(); j++) {
            if (prefixArray[j]==k) {
                count++;
            }
            int val = prefixArray[j] - k;

            if (prefixMap.find(val) != prefixMap.end()) {
                count+= prefixMap[val];
            } 
            if (prefixMap.find(prefixArray[j]) == prefixMap.end()) {
                prefixMap[prefixArray[j]]=0;
            }

            prefixMap[prefixArray[j]]++;
        }
        

        return count;
        
    }
};
// @lc code=end

