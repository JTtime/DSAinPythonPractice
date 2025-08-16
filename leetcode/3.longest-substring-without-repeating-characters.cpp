/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> myMap;
        int left = 0;
        int longestCount = 0;

        for (int i=0; i<s.size(); i++) {
            if ((myMap.count(s[i])>0) && (myMap[s[i]]>=left)) {
                left = myMap[s[i]]+1;
            }

            myMap[s[i]] = i;
            longestCount = std::max(longestCount, i-left+1);
        }

        return longestCount;
        
    }
};
// @lc code=end

