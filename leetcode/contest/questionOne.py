def main(nums):
    nums.sort(reverse=True)
    n=len(nums)
    k = n//3
    idx =1
    ans=0
    for i in range(1, 2*k, 2):
        ans+=nums[i]
    print(ans)
    
    
nums = [2,1,3,2,1,3]

main(nums)