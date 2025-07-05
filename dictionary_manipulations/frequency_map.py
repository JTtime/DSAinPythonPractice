numbers_list = [2,3,4,5,2,4,2,3,2,44,4,1,2,44,2,2,42,2,5]

# print(numbers_list[0])
result_dic={}
#for loop way of doing
for i in range(0,len(numbers_list)):
    # print(numbers_list[i])
    if numbers_list[i] in result_dic:
        result_dic[numbers_list[i]]+=1
    else:
        result_dic[numbers_list[i]]=1


print(result_dic)


one_liner_result={}

for i in range(0,len(numbers_list)):
    one_liner_result[numbers_list[i]] = one_liner_result.get(numbers_list[i], 0)+1


print("one liner result", one_liner_result)


