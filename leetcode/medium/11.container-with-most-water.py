#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        def min_value(a, b):
            if a < b:
                return a
            else:
                return b
        
        def max_value(a, b):
            if a > b:
                return a
            else:
                return b
            
        while left < right:
            width = right - left
            current_height = min_value(height[left], height[right])
            current_water = width * current_height
            max_water=max_value(current_water, max_water)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return max_water
# @lc code=end

