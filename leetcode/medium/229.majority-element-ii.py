#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_one = 0
        count_two = 0
        ans=[0]*2
        result=[]
        n = len(nums)
#finding probable answer values
        for i in range(0, n):
            if (count_one==0 and ans[1]!=nums[i]):
                ans[0]=nums[i]
                count_one=1
            elif (count_two==0 and ans[0]!=nums[i]):
                ans[1]=nums[i]
                count_two=1
            elif (ans[0]==nums[i]):
                count_one+=1
            elif  (ans[1]==nums[i]):
                count_two+=1
            else:
                count_one-=1
                count_two-=1

        
        count_a=0
        count_b=0

        #verification

        for i in range(0, len(nums)):
            if (ans[0]==nums[i]):
                count_a+=1
            elif(ans[1]==nums[i]):
                count_b+=1
            
        #edge cases, sometimes, we dont get two values > n/3 or cases like [1,2,3]
        if (count_a>n/3):
            result.append(ans[0])
        if(count_b>n/3):
            result.append(ans[1])

            
        

        return result



        
# @lc code=end

