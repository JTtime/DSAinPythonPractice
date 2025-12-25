#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_count = {}

        for i, num in enumerate(nums):
            compliment = target - num
            # count  = map_count.get(compliment, 0) + 1
            if compliment in map_count:
                return [i, map_count[compliment]]
            else:
                map_count[num] = i


# @lc code=end

