arr = [2,3,4,5,6,7,8,9,10,11]

target = 21

basket = {}

def two_sums_target(arr, target):
    n = len(arr)
    for i in range(0, n):
        check_other_number = target - arr[i]
        if check_other_number in basket:
            return [basket[check_other_number], i]
        else:
            basket[arr[i]] = i

        # print(i, arr[i])

print(two_sums_target(arr, target))
