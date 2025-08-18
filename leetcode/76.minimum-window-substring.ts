/*
 * @lc app=leetcode id=76 lang=typescript
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
function minWindow(s: string, t: string): string {
    let count = {};
    let ans = "";
    let windowLength = Number.MAX_SAFE_INTEGER;
    let ansWindowStart = 0;
    let left = 0;
    for (let i = 0; i < t.length; i++) {
    let ch = t[i];
    count[ch] = (count[ch] || 0) + 1;
}

    let missing = t.length;

    for (let right=0; right<s.length; right++) {
        let ch = s[right];
        if (count[s[right]]>0) {
            missing--;
        }
        count[ch] = (count[ch] || 0) - 1;


        while (missing==0) {
            
            if (right - left + 1 < windowLength) {
                ansWindowStart = left;
                windowLength = right - left + 1;
            }
            if (count[s[left]]>=0) {
                missing++;
            }
           count[s[left]]++;
            left++;
        }
    }


    return windowLength == Number.MAX_SAFE_INTEGER ? "" : s.substring(ansWindowStart, ansWindowStart+windowLength);
};
// @lc code=end

