def FindPattern(t,p):
    p_dict = {}
    for x in p:
        p_dict[x] = 0
    
    
    matches = {}
    start_i = 0
    end_i = 0
    for i in p:
        if i=="$":
            start_i=start_i+1
            continue
        break
    
    for j in range(len(p)-1,-1,-1):
        if p[j] == "$":
            end_i = end_i + 1
            continue
        break
    
    new_pattern = p.strip("$")
    if new_pattern == "":
        for i in range(0,len(t)-2,1):
            matched = ""
            for j in range(i,i+3,1):
                matched = matched+t[j]
            matches[matched] = 1
                
    else:
        last_pos = start_i+len(new_pattern)-1
        while(last_pos<len(t)-end_i):
            matched = ""
            j = len(new_pattern)-1
            i = last_pos
            while(i>=0):
                if t[i] == "$" or t[i] == new_pattern[j]:
                    matched = t[i] + matched
                    i=i-1
                    j=j-1
                else:
                    if not t[i] in p_dict:
                        last_pos = i+len(new_pattern)
                    else:
                        last_pos = last_pos + 1
                    break
                if j==-1:
                    for k in range(start_i):
                        matched = t[i-k]+matched
                    for k in range(end_i):
                        matched = matched+t[i+len(new_pattern)+k+1]
                    
                    matches[matched] = i - start_i + 1
                    last_pos = last_pos + 1
                    break
    result = []
    for i in matches.keys():
        result.append((matches[i],i))
    return result





T = "abcabe"
P = "$$$"
print(FindPattern(T,P))