# prices = [7,2,1,5,6,4,8]
# prices = [3, 2, 6, 1, 3]
# prices = [3, 3, 3, 3, 3]
prices = [2, 1, 2, 0, 1]

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

def maximum_of_two(a,b):
    if a>b:
        return a
    else:
        return b

def optimal_time(arr):
    lowest_price=arr[0]
    max_profit=float("-inf")
    for num in arr:        
        profit=num-lowest_price
        max_profit=maximum_of_two(max_profit, profit)
        if num<lowest_price:
            lowest_price=num
    

    print("optimal solution:", max_profit)


optimal_time(prices)
