#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = [0]*len(nums)
        prefixSum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefixSum[i] = nums[i] + prefixSum[i-1]
        
        prefixMap = {}
        
        for index, value in enumerate(prefixSum):
            if value==k :
                count+=1
            
            if (value-k) in prefixMap:
                count+=prefixMap[value-k]
            
            if (value not in prefixMap):
                prefixMap[value]=0
            
            prefixMap[value]+=1
        
        return count
                
        
# @lc code=end

