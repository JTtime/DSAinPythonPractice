#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map={}
        left=0
        longestCount = 0
        
        for right, fruit in enumerate(fruits):
            
            
            if fruit not in map and len(map)==2:
                fruit_to_remove=min(map, key=map.get)
                lastSeenIndex = map.pop(fruit_to_remove)
                left = lastSeenIndex + 1
                
            map[fruit]=right #add new fruit
            longestCount=max(longestCount, right-left + 1)
            
        
        return longestCount
                
                
        
# @lc code=end

