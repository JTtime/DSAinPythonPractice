numbers_list = [2,3,4,5,2,4,2,3,2,44,4,1,2,44,2,2,42,2,5]

#recursive approach to reverse array

def swap_nums(array, l, r):
    if r>l:
        array[l], array[r] = array[r], array[l]
        return swap_nums(array, l+1, r-1)
        # swap_nums(array, l+1, r-1)
    else:
        return array
        # return
    



reversed_array = swap_nums(numbers_list, 0, len(numbers_list)-1)

# print(numbers_list) List is passed by reference so both approach gives same answers
print(reversed_array)


def loop_reverse(array, l, r):
    while r>l:
        array[l], array[r], array[r], array[l]
        l+=1
        r-=1

    # return array

# print("loop:",loop_reverse(numbers_list, 0, len(numbers_list)-1))
loop_reverse(numbers_list, 0, len(numbers_list)-1)
print("loop:",numbers_list)