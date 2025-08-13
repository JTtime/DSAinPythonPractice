n, k = map(int, input().split())



count=0

scores=list(map(int, input().split()))

target = scores[k-1]

for idx, val in enumerate(scores):
    if val==0:
        break
    if(val<target):
        break
    else:
        count+=1


print(count)

# for i in range(n):
#     score=int(input())
#     if score==0:
#         break
#     if (i==(k-1)):
#         target=score
    
#     if(score>target):
#         count+=1


# print(count)
        
    