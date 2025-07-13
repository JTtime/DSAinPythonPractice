/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
    
public:
        int max_value(int a, int b) {
            if (a>b) {
                return a;
            } else {
                return b;
            }
        }

        int min_value(int a, int b) {
            if (a<b) {
                return a;
            } else {
                return b;
            }
        }
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;
        
        


        while (left<right) {
            int width = right - left;
            int min_height = min_value(height[right], height[left]);
            int current_water = width * min_height;
            maxArea = max_value(current_water, maxArea);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }            
        }
        return maxArea;
    }
};
// @lc code=end

