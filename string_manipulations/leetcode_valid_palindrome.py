s = "A man, a plan, a canal: Panama"

def valid_palindrome(s: str) -> bool:
    i, j = 0, len(s) -1
    
    
    while (i<=j):
        if (not s[i].isalnum()):
            i+=1
            continue
        if (not s[j].isalnum()):
            j-=1
            continue
        if s[i].lower() != s[j].lower():
            return False       
        
        print("i: ", s[i].lower(), "j: ", s[j].lower())
        i, j = i+1, j-1
    
    return True



print(valid_palindrome(s))