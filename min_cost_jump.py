def minCost(H):

    if len(H)==2:
        print(H)
        print(abs(H[0]-H[1]))
        return abs(H[0]-H[1])
    t_cost = min(abs(H[0] - H[len(H)-1]), abs(minCost(H[0:len(H)-1])+ abs(H[len(H)-2]-H[len(H)-1])))
    print("====================")
    print("cost of going to ", H[len(H)-1])
    print(t_cost)
    print("====================")
    return t_cost


    
        
        

H = eval(input())
print(minCost(H))