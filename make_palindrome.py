def MakePalindrome(s):
    s_length = len(s)
    l = len(s)
    prefix_pos = len(s)-1
    is_palindrome = True
    while(l>0):
        if s_length ==0 or s_length-l == l-1 or l-1<s_length-l:
            break
        elif s[s_length-l] != s[l-1]:
            is_palindrome = False
            prefix_pos = l-1
            s_length = l-1
        l=l-1
    if is_palindrome:
        return None
    prefix = ""
    for i in range(len(s)-1,prefix_pos-1,-1):
        prefix = prefix + s[i]
    return prefix
        
print(MakePalindrome("bcdefghijkllkjihgfedcba"))
