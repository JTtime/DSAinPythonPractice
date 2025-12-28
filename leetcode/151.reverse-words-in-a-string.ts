/*
 * @lc app=leetcode id=151 lang=typescript
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
function reverseWords(s: string): string {
    return s.trim().split(/\s+/).reverse().join(" ")
    // split(" ") just splits it with one whitespace, so implemented regex for removing leading and trailing spaces for all words
};
// @lc code=end

