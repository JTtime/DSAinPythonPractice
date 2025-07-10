#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reversed_x=0
        if x<0:
            return False
        while (num>0):
            last_digit=num%10
            num=num//10
            reversed_x=(reversed_x*10)+last_digit
        

        if reversed_x==x:
            return True
        else:
            return False

            
            
# @lc code=end

