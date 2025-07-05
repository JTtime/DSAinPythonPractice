n = [2,3,4,5,2,4,2,3,2,44,4,1,2,4,2,2,4,2,5]

m = [2,3,4,6,9]

#brute force method

# ans_dic={}

# for num in m:
#     count=0
#     for x in n:
#         if num==x:
#             count+=1            
#             # ans_dic[num]=ans_dic.get(num,0)+1   # uncommenting this line will ignore zero values in dictionary output, because it is inside if condition
            
    
  
#     ans_dic[num]=count # uncomenting this line includes zero values like 6 and 9 in dictionary


# print(ans_dic)

hash_list=[0]*11

# result_hash={}

# for num in m:
#     result_hash[num] = n.count(num) time complexity is O(n * m)

#following is time complexity O(n+m)
for num in m:
    hash_list[num]+=1

for num in n:
    if (1<=num<=10) and hash_list[num]!=0:
        hash_list[num]+=1


for num in m:
    hash_list[num]-=1



print("hash List",hash_list)





