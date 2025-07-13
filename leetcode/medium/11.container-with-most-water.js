/*
 * @lc app=leetcode id=11 lang=javascript
 *
 * [11] Container With Most Water
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max_water = 0;

    while (left<right) {
        let width = right - left;
        let current_height = Math.min(height[left], height[right]);
        let current_water = current_height*width
        max_water=Math.max(max_water, current_water);

        if (height[left]<height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return max_water;
    
};
// @lc code=end

