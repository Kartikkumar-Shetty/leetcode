def FindPattern(t,p):
    p_dict = {}
    for x in p:
        p_dict[x] = 0
    
    
    matches = {}
    
    last_pos = len(p)-1
    
    while(last_pos<len(t)):
        matched = ""
        j = len(p)-1
        i = last_pos
        while(i>=0):
            if p[j] == "$" or t[i] == p[j]:
                matched = t[i] + matched
                i=i-1
                j=j-1
            else:
                curr_count = 0
                if not t[i] in p_dict:
                    last_pos = i+len(p)
                else:
                    last_pos = last_pos + 1
                break
            if j==-1:
                matches[matched] = i + 1
                last_pos = last_pos + 1
                break
    result = []
    for i in matches.keys():
        result.append((matches[i],i))
    return result




T = input()
P = input()
print(FindPattern(T,P)) 