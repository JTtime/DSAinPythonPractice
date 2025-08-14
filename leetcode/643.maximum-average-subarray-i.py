#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        
        for i in range(k):
            sum+=nums[i]
        
        maxSum=sum
        
        for i in range(k, len(nums)):
            sum+=nums[i]-nums[i-k]
            maxSum=max(sum, maxSum)
        
        return maxSum/k
        
# @lc code=end

