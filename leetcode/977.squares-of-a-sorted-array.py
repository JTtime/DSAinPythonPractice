#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        ans = [None]*len(nums)
        k = j
        while (i<=j):
            if (abs(nums[i]) > abs(nums[j])):
                ans[k] = nums[i]*nums[i]
                i+=1
            else:
                ans[k] = nums[j]*nums[j]
                j-=1
            k-=1
        
        return ans
# @lc code=end

