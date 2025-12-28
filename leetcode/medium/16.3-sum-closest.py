#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float('inf')
        ans = target
        nums.sort()

        for i, num in enumerate(nums):
            j = i+1
            k = len(nums) - 1
            while j < k:
                new_sum = nums[i] + nums[j] + nums[k]
                
                if new_sum == target:
                    return new_sum
                elif new_sum < target:
                    j+=1
                elif new_sum > target:
                    k-=1
                if abs(target - new_sum) < abs(min_diff):
                    min_diff = abs(target - new_sum)
                    ans = new_sum            
                    
        return ans
# @lc code=end

