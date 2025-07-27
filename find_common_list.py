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
    
def final_merge(L1,L2):
    i=0
    j=0
    L3 = []
    while True:
        if i==len(L1):
            break
        if j==len(L2):
            break
        if L1[i]<L2[j]:
            i=i+1
        elif L1[i]>L2[j]:
            j=j+1
        else:
            L3.append(L1[i])
            i=i+1
            j=j+1
    return L3    

def findCommonElements(L1, L2):
    L1 = split_and_merge(L1)
    L2 = split_and_merge(L2)
    L3 = final_merge(L1,L2)
    print(L3)
        
findCommonElements([3, 7, 2, 9, 5],[6, 3, 7, 5, 4])


