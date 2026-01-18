#User function Template for python3
#https://www.geeksforgeeks.org/problems/geeks-training/1

class Solution:
    def maximumPoints(self, arr):
        # Code here
        
        
        n = len(arr)
        dp = [[-1]*4 for _ in range(n)]
        
        def training(idx, last, dp):
            # maxi=0
            # if idx==n-1:
            #     for i in range(0,3):
            #         if i!=last:
            #             maxi=max(maxi, arr[n-1][i])
                
            #     return maxi
            if idx==n:
                return 0
            
            if dp[idx][last]!=-1:
                return dp[idx][last]
            
            
            maxi=0
            for i in range(0,3):
                if i!=last:
                    # maxi=max(maxi, (training(idx+1, i) + arr[idx][i]))
                    maxi=max(maxi, (training(idx+1, i, dp) + arr[idx][i]))
            dp[idx][last] = maxi
            return maxi
            
        
        return training(0, 3, dp)
    
    
    #tabulation approach
    
    lass Solution:
    def maximumPoints(self, arr):
        # Code here
        
        
            n = len(arr)
            dp = [[-1]*4 for _ in range(n+1)]
        
        
            
            #dp[n][last] = 0   for all last ∈ {0,1,2,3}

            for i in range(4):
                dp[n][i] = 0
            # return 0
            
            
            
            for idx in range(n-1, -1, -1):
                for last in range(4):
                    maxi=0
                    for i in range(3):
                        if i!=last:
                            maxi = max(maxi, (dp[idx+1][i] + arr[idx][i]))
                    dp[idx][last] = maxi
            return dp[0][3]
            
                