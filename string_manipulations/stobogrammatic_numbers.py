a = "69"  #true

b = "808" #true

c ="96269" #false

d = "101" #True


def check_stobo(s):
    i, j = 0, len(s) - 1
    non_stobo = ["2", "3", "4", "5", "7"]
    mirrored_stobo = ["6", "9"]
    stobo = ["0", "1", "8"]
    
    while (i<=j):
        if s[i] in non_stobo or s[j] in non_stobo:
            return False
        if (len(s)%2!=0)  and (i == j) and (s[i] in non_stobo or s[i] in mirrored_stobo):   # middle character if its odd length
            return False
        if (s[i] in mirrored_stobo and s[j] in mirrored_stobo) or (s[i] in stobo and s[j] in stobo):
            i+=1
            j-=1
            continue
    
    return True


print(check_stobo(d))
        
            
    

