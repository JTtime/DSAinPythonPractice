#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count_red, count_white, count_blue = 0, 0, 0

        # for num in nums:
        #     if num == 0:
        #         count_red+=1
        #     elif num == 1:
        #         count_white+=1
        #     elif num == 2:
        #         count_blue+=1
        
        # for i in range(count_red):
        #     nums[i] = 0
        # for i in range(count_red, count_red+count_white):
        #     nums[i] = 1
        # for i in range(count_red+count_white, count_red+count_white+count_blue):
        #     nums[i] = 2
        
        #alternate solution
        
        i, j , k = 0, len(nums)-1, 0
        
        while k<=j:
            if nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j-=1
            elif nums[k] == 1:
                k+=1
            else:
                if i == k:
                    i+=1
                    k+=1
                elif i < k:
                    nums[i], nums[k] = nums[k], nums[i]
                    i+=1
                
            

# @lc code=end

