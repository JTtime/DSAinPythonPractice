/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longestCount = 0;
        int left = 0;
        unordered_map<char, int> myMap;

        for (int right=0; right<s.size(); right++) {
            if (myMap.count(s[right])>0) {
                myMap[s[right]]=right;
            }
            if ((myMap.count(s[right])==0) && (myMap.size()<2)) {
                myMap[s[right]]=right;
            }
            if ((myMap.count(s[right])==0) && (myMap.size()==2)) {
                auto min_it = std::min_element(
                myMap.begin(), myMap.end(),
                [](const auto& a, const auto& b) {
                    return a.second < b.second;
                };

                myMap.erase(min_it);
                myMap[s[right]] = right;
                left = min_it->second+1;
            );
        }
        longestCount=std::max(longestCount, right-left+1);
        
    }
    return longestCount;
};
}
// @lc code=end

