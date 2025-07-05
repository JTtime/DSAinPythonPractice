n = [2,3,4,5,2,4,2,3,2,44,4,1,2,44,2,2,42,2,5]

m = [2,3,5,4,6,9]

ans_dic={}

for num in m:
    count=0
    for x in n:
        if num==x:
            count+=1            
            # ans_dic[num]=ans_dic.get(num,0)+1   # uncommenting this line will ignore zero values in dictionary output, because it is inside if condition
            
    
  
    ans_dic[num]=count # this line includes zero values like 6 and 9 in dictionary


print(ans_dic)

