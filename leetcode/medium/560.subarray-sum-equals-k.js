/*
 * @lc app=leetcode id=560 lang=javascript
 *
 * [560] Subarray Sum Equals K
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let ans = 0;
    let prefixArray = [nums[0]];
    let prefixMap = {};

    for(let i=1; i<nums.length; i++) {        
        prefixArray.push(nums[i] + prefixArray[i-1]);
    }

    for (let j=0; j<prefixArray.length; j++) {
        if (prefixArray[j]==k) {
            ans++;
        }
        if (prefixMap.hasOwnProperty(prefixArray[j] - k)) {
            ans+= prefixMap[prefixArray[j]-k]
            

        } 
        if (!prefixMap.hasOwnProperty(prefixArray[j])) {
            prefixMap[prefixArray[j]] = 0
        }

        prefixMap[prefixArray[j]] = (prefixMap[prefixArray[j]] || 0) + 1;

    }



    return ans;
    
};
// @lc code=end

