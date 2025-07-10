/*
 * @lc app=leetcode id=9 lang=javascript
 *
 * [9] Palindrome Number
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let num = x
    if (x<0) {
        return false;
    }
    let reversed_x=0
    while (num>0) {
        let last_digit = num%10
        num= Math.floor(num/10);
        reversed_x = (reversed_x*10)+last_digit
        
    }
    if (reversed_x==x) {
        return true
    } else {return false}
};
// @lc code=end

