#gfg https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1


def countTriplets(self, n, sum, arr):
        #code here
        ans = float('-inf')
        arr.sort()
        count = 0
        for i, num in enumerate(arr):
            j = i+1
            k= len(arr) - 1
            
            while j < k:
                new_sum = arr[i] + arr[j] + arr[k]
                
                if new_sum>=sum:
                    k-=1
                else:
                    count+=k-j
                    j+=1
                
        return count