# prices = [7,2,1,5,6,4,8]
prices = [7, 1, 5, 3, 6, 4]

#brute force
def best_time(arr):
    max_profit=float("-inf")
    head=0
    tail=0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if max_profit<(arr[j]-arr[i]):
                max_profit=arr[j]-arr[i]
                head=arr[i]
                tail=arr[j]
                


    print("brute forcr:", max_profit, head, tail)       



best_time(prices)