def merge_and_sort(items):
    if len(items)==1:
        return items
    m = len(items)//2
    m1 = merge_and_sort(items[0:m])
    m2 = merge_and_sort(items[m:len(items)])
    return merge(m1,m2)

def merge(m1,m2):
    i=0
    j=0
    m3 = []
    while True:
        if i==len(m1):
           m3 = m3 + m2[j:len(m2)] 
           break
        if j==len(m2):
           m3 = m3 + m1[i:len(m1)] 
           break
        if m1[i][1]/m1[i][0]>=m2[j][1]/m2[j][0]:
           m3.append(m1[i])
           i=i+1
        else:
           m3.append(m2[j])
           j=j+1
            
    return m3

def MaxValueSelection(items, C):
    arr = []
    for i in items.keys():
        arr.append(items[i])
    s_items = merge_and_sort(arr)
    price = 0
    while (C>0):
        for j in range(len(s_items)):
            if C>=s_items[j][0] and s_items[j][0]>0:
                price = price + s_items[j][1]
                C=C-s_items[j][0]
                s_items[j] = (0,s_items[j][1])
            elif C<s_items[j][0]:
                per_val = s_items[j][1]/s_items[j][0]
                price = price + C*per_val
                C=0
    return price
                


items = {1:(10,60),2:(20,100),3:(30,120)}
C = 50
print(round(MaxValueSelection(items, C),2))