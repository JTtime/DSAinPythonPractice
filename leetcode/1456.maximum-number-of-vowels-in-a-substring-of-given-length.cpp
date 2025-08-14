/*
 * @lc app=leetcode id=1456 lang=cpp
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 */

// @lc code=start
#include <algorithm>
class Solution {
public:
    int maxVowels(string s, int k) {
        char vowels[5] = {'a', 'u', 'o', 'i', 'e'};
        int vowelCount = 0;
        for (int i=0; i<k; i++) {
            if (std::find(std::begin(vowels), std::end(vowels), s[i]) != std::end(vowels)) {
                vowelCount++;
            }
        }

        int maxCount = vowelCount;


        for (int i=k; i<s.size(); i++) {
            if (std::find(std::begin(vowels), std::end(vowels), s[i-k]) != std::end(vowels)) {
                vowelCount--;
            }
            if (std::find(std::begin(vowels), std::end(vowels), s[i]) != std::end(vowels)) {
                vowelCount++;
            }

            maxCount=std::max(maxCount, vowelCount);

        }

        return maxCount;



    }
};
// @lc code=end

