def knapSack(W,weight,values,N):
    if sum(weight)>W:
        profit= []
        if len(weight)==1:
            return 0
        for i in range(N):
            t_weight = weight[0:i] + weight[i+1:len(weight)]
            t_values = values[0:i] + values[i+1:len(values)]
            profit.append(knapSack(W,t_weight,t_values,N-1))
        
        return max(profit)
    else:
        p = 0
        for i in range(len(weight)):
            p = p + values[i]
        return p
        



N=int(6)
W=int(10)
weight=[4,4,5,6,7,2]
values=[50,40,60,6,91,2]
print(knapSack(W,weight,values,N))