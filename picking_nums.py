def split_and_merge(L):
    if len(L)==1:
        return [L[0]]

    mid = len(L)//2
    L1 = split_and_merge(L[0:mid])
    L2 = split_and_merge(L[mid:len(L)])
        
    L3 = merge(L1,L2)
    return L3

def merge(L1,L2):
    L3 = []
    i=0
    j=0
    while True:
        if i==len(L1):
            L3 = L3+L2[j:len(L2)]
            break
        if j==len(L2):
            L3 = L3+L1[i:len(L1)]
            break
        if L1[i]<L2[j]:
            L3.append(L1[i])
            i=i+1
        else:
            L3.append(L2[j])
            j=j+1
    return L3
def pickingNumbers(a):
    LL = []
    L = split_and_merge(a)
    LL.append([L[0]])
    i=0
    j=1
    
    while not j==len(L):
        if abs(L[i]-L[j])<=1:
            if len(LL[i])==1:
                if j-i>1:
                    LL[i] = LL[i] + L[i+1:j+1]
            LL[i].append(L[j])
            j=j+1
        else:
            i=i+1
            if i==j:
                j=j+1
            LL.append([L[i]])
    print(LL)
    max_len = 0
    max_arr = 0
    for i in range(len(LL)):
        if len(LL[i])>max_len:
            max_len = len(LL[i])
            max_arr = LL[i]
    print(max_arr)
    return max_len
            
    

a=[9,6,13,16,5,18,4,10,3,19,4,5,8,1,13,10,20,17,15,10,6,10,13,20,18,17,7,10,6,5,16,18,13,20,19,7,16,13,20,17,4,17,8,19,12,7,17,1,18,3,16,4,5,3,15,17,6,17,14,11,11,7,11,6,15,15,12,6,17,19,8,6,13,9,10,19,14,18,7,9,11,16,11,20,4,20,10,7,8,4,2,12,11,8,12,13,19,8,8,5]
print(pickingNumbers(a))