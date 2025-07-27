# considering dictionary as a heap for given code

def min_heapify(i,size):

    lchild = 2*i + 1

    rchild = 2*i + 2

    small = i

    if lchild < size-1 and HtoV[lchild][1] < HtoV[small][1]: 

        small = lchild

    if rchild < size-1 and HtoV[rchild][1] < HtoV[small][1]: 

        small = rchild

    if small != i:

        VtoH[HtoV[small][0]] = i

        VtoH[HtoV[i][0]] = small

        (HtoV[small],HtoV[i]) = (HtoV[i], HtoV[small])

        min_heapify(small,size)


def create_minheap(size):

    for x in range((size//2)-1,-1,-1):

        min_heapify(x,size)


def minheap_update(i,size):

    if i!= 0:

        while i > 0:

            parent = (i-1)//2

            if HtoV[parent][1] >  HtoV[i][1]:

                VtoH[HtoV[parent][0]] = i

                VtoH[HtoV[i][0]] = parent

                (HtoV[parent],HtoV[i]) = (HtoV[i], HtoV[parent])

            else:

                break

            i = parent


def delete_min(hsize):

    VtoH[HtoV[0][0]] = hsize-1

    VtoH[HtoV[hsize-1][0]] = 0

    HtoV[hsize-1],HtoV[0] = HtoV[0],HtoV[hsize-1]  

    node,dist = HtoV[hsize-1]

    hsize = hsize - 1

    min_heapify(0,hsize) 

    return node,dist,hsize


#global HtoV map heap index to (vertex,distance from source)

#global VtoH map vertex to heap index

HtoV, VtoH = {},{}

def dijkstra(WMat,s):

    (rows,cols,x) = WMat.shape

    infinity = float('inf')

    visited = {}

    heapsize = rows

    for v in range(rows):

        VtoH[v]=v

        HtoV[v]=[v,infinity]

        visited[v] = False

    HtoV[s]= [s,0]

    create_minheap(heapsize)

    

    for u in range(rows):

        nextd,ds,heapsize = delete_min(heapsize)             

        visited[nextd] = True        

        for v in range(cols):

            if WMat[nextd,v,0] == 1 and (not visited[v]):

                # update distance of adjacent of v if it is less than to previous one

                HtoV[VtoH[v]][1] = min(HtoV[VtoH[v]][1],ds+WMat[nextd,v,1])

                minheap_update(VtoH[v],heapsize)



dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]

#edges = dedges + [(j,i,w) for (i,j,w) in dedges]

size = 7

import numpy as np

W = np.zeros(shape=(size,size,2))

for (i,j,w) in dedges:

    W[i,j,0] = 1

    W[i,j,1] = w

s = 0

dijkstra(W,s)

#print(HtoV)

#print(VtoH)

for i in range(size):

    print('Shortest distance from {0} to {1} = {2}'.format(s,i,HtoV[VtoH[i]][1]))
    

