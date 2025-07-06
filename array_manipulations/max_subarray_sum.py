arr = [-2,3,-4,5,6,7,8,-9,10,11]

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
# print("head and tail", head, tail, arr[head:tail+1])


