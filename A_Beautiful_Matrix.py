
for innerIdx, val in enumerate(range(5), start=1):
    row = list(map(int, input().split()))
    
    for outerIdx, val in enumerate(row, start=1):
        if val==1:
            print(abs(innerIdx-3)+abs(outerIdx-3))