def primlist2(WList):

    # Initialization

    infinity = float("inf")

    (visited,distance,nbr) = ({},{},{})

    for v in WList.keys():

        (visited[v],distance[v],nbr[v]) = (False,infinity,-1)

    

    # Set start vertex distance to 0 

    distance[0] = 0

    

    # Repeat the below process (number of vertices-1) times

    for i in range(0,len(WList.keys())):

        # Find minimum distance value on vertices which are not visited

        min_dist = min([distance[v] for v in WList.keys() if not visited[v]])

        

        # Find all vertices that have minimum distance value min_dist and not visited

        nextv_list = [v for v in WList.keys() if (not visited[v]) and distance[v] == min_dist]

        

        # Select the minimum level value vertex from nextv_list ans mark visited

        nextv = min(nextv_list)      

        visited[nextv] = True

        

        # Update the nbr or parent value for v with minimum eadge distance

        for (v,d) in WList[nextv]:

            if not visited[v]:

                if d < distance[v]:

                    nbr[v] = nextv

                    distance[v] = d

    return(nbr)




dedges = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]

edges = dedges + [(j,i,w) for (i,j,w) in dedges]

size = 5

WL = {}

for i in range(size):

    WL[i] = []

for (i,j,d) in edges:

    WL[i].append((j,d))

print(primlist2(WL))