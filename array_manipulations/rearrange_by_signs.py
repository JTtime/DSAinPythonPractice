nums = [5,10,-3, -1, -10, 6]
result=[0]*len(nums)
# In Python, you can't assign to an index in a list that doesn't exist yet. You must either:

# Pre-fill the list with placeholders (like 0s)

# Or use .append() instead of direct indexing

def rearrange(arr):
    neg=[]
    pos=[]    
    for i in range(0, len(arr)):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    

    for i in range(0, len(pos)):
        result[2*i]=pos[i]
        result[(i*2)+1]=neg[i]
    
    print("result:", result)


rearrange(nums)
