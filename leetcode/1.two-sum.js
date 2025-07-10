/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const basket = {}
    let head = 0
    let tail = 0
    for (let i=0; i<nums.length; i++) {
        const check_other_number = target - nums[i];
        if (basket.hasOwnProperty(check_other_number)) {
            head = basket[check_other_number]
            tail = i
        } else {
            basket[nums[i]]=i
        }
    }

    return [head, tail]
};
// @lc code=end

