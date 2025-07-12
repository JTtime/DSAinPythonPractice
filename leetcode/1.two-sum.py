#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        basket = {}
        head = 0
        tail=0
        

        for index, num in enumerate(nums):
            check_other_number=target-num
            if check_other_number in basket:
                head = basket[check_other_number]
                tail = index
            else:
                basket[num] = index
            
        return [head, tail]
    
    #Use following solution if given array is sorted

        # tail = len(nums)-1
        # while (head<tail):
        #     if (nums[head]+nums[tail]==target):
        #         print([head, tail])
        #         return[head, tail]
        #     elif ((nums[head]+nums[tail])<target):
        #         head+=1
        #     elif((nums[head]+nums[tail])>target):
        #         tail=tail-1

        
# @lc code=end

