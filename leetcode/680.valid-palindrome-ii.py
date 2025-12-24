#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def valid_palindrome(self, s, i , j):
    # i, j = 0, len(s) - 1
    
        while (i<=j):
            if (not s[i].isalnum()):
                i+=1
                continue
            if (not s[j].isalnum()):
                j-=1
                continue
            if (s[i].lower() != s[j].lower()):
                return False
            i+=1
            j-=1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
    
        while (i<=j):
            if (s[i].lower() == s[j].lower()):
                i+=1
                j-=1
            else:
                return self.valid_palindrome(s, i, j-1) or self.valid_palindrome(s, i+1, j)
        
        return True
        
        
# @lc code=end

