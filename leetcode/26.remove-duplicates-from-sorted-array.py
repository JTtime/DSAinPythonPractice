#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k = 0, 1, 1
        
        while j < len(nums):
            if nums[j] == nums[j-1]:
                j+=1
            else:
                nums[i+1] = nums[j]
                k+=1
                j+=1
                i+=1
        
        return k
            
            
            
            
# @lc code=end

