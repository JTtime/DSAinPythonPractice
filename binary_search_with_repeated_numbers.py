number_list = [4,4,4,4,4,4,4,4,4,12,56,234,675,789, 799, 800, 812, 832]





def find_number(list_of_numbers, target):
    lo, hi = 0, len(list_of_numbers) - 1
    result = -1

    while lo <= hi:
        mid=(lo+hi)//2
        mid_number=list_of_numbers[mid]
        print("Lo:", lo, "hi:", hi, "mid:", mid, "mid_number:", mid_number)

        if mid_number==target:
            result = mid #instead of returning result directly, just save it
            hi=mid-1 # keep looking on left side
        elif mid_number<target:
            lo=mid+1
        elif mid_number>target:
            hi=mid-1
    

    return result

ans = find_number(number_list, 5)
print("ANS:", ans)
