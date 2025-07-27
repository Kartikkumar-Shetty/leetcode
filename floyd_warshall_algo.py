def floydwarshall(WMat):

    # Initialization

    (rows,cols,x) = WMat.shape

    infinity = float('inf')  

    SP = np.zeros(shape=(rows,cols,cols+1))

    

    # Filling the initial graph entry in matrix

    for i in range(rows):

        for j in range(cols):

            if WMat[i,j,0] == 1:

                SP[i,j,0] = WMat[i,j,1]

            else:

                SP[i,j,0] = infinity

    

    # Repeat the process n times where n is number of vertices

    for k in range(1,cols+1):

        # Checking The shortest path distance for each pair in matrix 

        for i in range(rows):

            for j in range(cols):

                SP[i,j,k] = min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])

    

    # Retuen the last updated matrix

    return(SP[:,:,cols])



edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]

size = 7

import numpy as np
W = np.zeros(shape=(size,size,2))


for (i,j,w) in edges:

    W[i,j,0] = 1

    W[i,j,1] = w    

print(floydwarshall(W))