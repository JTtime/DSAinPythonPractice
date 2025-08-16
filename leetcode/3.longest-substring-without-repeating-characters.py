#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map={}
        longestCount=0
        left=0
        for right, ch in enumerate(s):
            if (ch in map) and (map[ch]>=left):
                left = map[ch] + 1
            
            map[ch]=right
            longestCount=max(longestCount, right-left+1)
        
        
        return longestCount
                
        
# @lc code=end

