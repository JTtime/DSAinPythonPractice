#
# @lc app=leetcode id=2824 lang=python3
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        nums.sort()
        count = 0

        while (i<j):
            if ((nums[i] + nums[j]) < target):
                count += j - i
                i = i + 1
            else:
                j = j - 1
        
        return count
# @lc code=end

