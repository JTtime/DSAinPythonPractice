#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        col_start=0
        col_end= n-1
        row_start=0
        row_end = m-1
        a = []



        while (col_start<=col_end) and (row_start<=row_end):

            for i in range(col_start, col_end+1):
                num = matrix[row_start][i]
                a.append(num)
                            
            row_start+=1

            for i in range(row_start, row_end+1):
                num = matrix[i][col_end]
                a.append(num)
                        
            col_end-=1
            
            if row_start <= row_end:
                for i in range(col_end, col_start-1, -1):
                    num = matrix[row_end][i]
                    a.append(num)
                row_end-=1
            
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    num = matrix[i][col_start]
                    a.append(num)
                col_start+=1

            
            
        
        return a
# @lc code=end

