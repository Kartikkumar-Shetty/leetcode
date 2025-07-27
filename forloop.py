def findContinuousRepetitions(t,p):
    p_dict = {}
    for x in p:
        p_dict[x] = 0
    last_pos = len(p)-1

    max_count = 0
    curr_count = 0
    while(last_pos<len(t)):
        j = len(p)-1
        i = last_pos
        while(i>=0):
            if t[i] == p[j]:
                i=i-1
                j=j-1
            else:
                curr_count = 0
                if not t[i] in p_dict:
                    last_pos = i+len(p)
                else:
                    last_pos = last_pos + 1
                break
            if j==0:
                curr_count = curr_count + 1
                if curr_count>max_count:
                    max_count = curr_count
                last_pos = last_pos + len(p)
                break
    return max_count
        


t = input()
p = input()
print(findContinuousRepetitions(t, p))