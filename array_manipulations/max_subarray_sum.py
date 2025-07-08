arr = [-2,3,-4,5,6,7,8,9,-10,11]

max=arr[0]
head = 0
tail = 0

for i in range(0, len(arr)-1):
    sum_in_loop=arr[i]
    max_sum_in_loop=arr[i]
    for j in range(i+1, len(arr)):
        if max_sum_in_loop < (sum_in_loop + arr[j]):
            max_sum_in_loop = sum_in_loop + arr[j]
            # tail = j
            # head=i

        sum_in_loop=sum_in_loop+arr[j]
        
    
    if max<max_sum_in_loop:
        max=max_sum_in_loop
        # head = i



print("max:", max)
def maximum_of_two(a,b):
    if a>b:
        return a
    else:
        return b

def kanade():
    max_sum=0
    current_sum=0
    for num in arr:
        if current_sum<0:
            current_sum=0
        else:
            current_sum+=num
            max_sum = maximum_of_two(max_sum, current_sum)
    

    print("current_sum:",max_sum)



kanade()


# print("head and tail", head, tail, arr[head:tail+1])


