def dijkstra(WMat,s):

    (rows,cols,x) = WMat.shape

    infinity = np.max(WMat)*rows+1

    (visited,distance) = ({},{})

    for v in range(rows):

        (visited[v],distance[v]) = (False,infinity)

        

    distance[s] = 0

    

    for u in range(rows):

        nextd = min([distance[v] for v in range(rows)

                        if not visited[v]])

        nextvlist = [v for v in range(rows)

                        if (not visited[v]) and

                            distance[v] == nextd]

        if nextvlist == []:

            break

        nextv = min(nextvlist)

        

        visited[nextv] = True        

        for v in range(cols):

            if WMat[nextv,v,0] == 1 and (not visited[v]):

                distance[v] = min(distance[v],distance[nextv]

                                              +WMat[nextv,v,1])

    return(distance)



dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]

#edges = dedges + [(j,i,w) for (i,j,w) in dedges]

size = 7

import numpy as np

W = np.zeros(shape=(size,size,2))

for (i,j,w) in dedges:

    W[i,j,0] = 1

    W[i,j,1] = w

s = 0

print(dijkstra(W,s))