/*
 * @lc app=leetcode id=904 lang=cpp
 *
 * [904] Fruit Into Baskets
 */

// @lc code=start
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int longestCount = 0;
        int left = 0;
        unordered_map<int, int> myMap;

        for (int right=0; right<fruits.size(); right++) {
            
            if ((myMap.count(fruits[right])==0) && (myMap.size()==2)) {
                auto min_it = std::min_element(
                myMap.begin(), myMap.end(),
                [](const auto& a, const auto& b) {
                    return a.second < b.second;
                });               
                left = (min_it->second)+1;
                myMap.erase(min_it);
        }
         myMap[fruits[right]] = right;
        longestCount=std::max(longestCount, right-left+1);
    };
    return longestCount;
    }
};
// @lc code=end

