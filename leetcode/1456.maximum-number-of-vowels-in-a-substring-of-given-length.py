#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_list = ["a", "e", "i", "o", "u"]
        count=0
        for i in range(k):
            if s[i] in vowels_list:
                count+=1
        
        maxCount = count

        for i in range(k, len(s)):
            if s[i] in vowels_list:
                count+=1
            
            if s[i-k] in vowels_list:
                count-=1
            
            maxCount = max(count, maxCount)
        

        return maxCount
# @lc code=end

