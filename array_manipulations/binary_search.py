number_list = [2,4,12,56,234,675,789, 799, 800, 812, 832]

def find_number(list_of_numbers, target):
    lo, hi = 0, len(list_of_numbers) - 1

    while lo <= hi:
        mid=(lo+hi)//2
        mid_number=list_of_numbers[mid]
        print("Lo:", lo, "hi:", hi, "mid:", mid, "mid_number:", mid_number)

        if mid_number==target:
            return mid
        elif mid_number<target:
            lo=mid+1
        elif mid_number>target:
            hi=mid-1
    

    return -1

ans = find_number(number_list, 4)
print("ANS:", ans)
