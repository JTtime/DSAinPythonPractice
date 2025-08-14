/*
 * @lc app=leetcode id=1456 lang=javascript
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    let vowelsCount = 0;
    for (let i=0; i<k; i++) {
        if (vowels.includes(s[i])) {
            vowelsCount++;
        }
    }
    let maxVowels = vowelsCount;

    for (let i=k; i<s.length; i++) {
        if (vowels.includes(s[i-k])) vowelsCount--;
        if (vowels.includes(s[i])) vowelsCount++;
        maxVowels = Math.max(vowelsCount, maxVowels)
    }

    return maxVowels;
    
    
};
// @lc code=end

