t = int(input())

for _ in range(t):
    n, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr_length = len(arr)
    max_value =  arr[0]
    
    for x in arr:
        if x>max_value:
            max_value=x
        
    
    if (k>1) or (k==1 and arr[j-1]==max_value):
        print("YES")
    else:
        print("NO")
    
    
    
        



    





