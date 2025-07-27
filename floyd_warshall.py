# Algorithm Steps

# Here are the steps for the algorithm:

#     Initialization: Create a 2-dimensional array SP of size n x n, where n is the number of vertices in the graph. For each pair of vertices (i,j), initialize SP[i][j] to the weight of the edge from vertex i to vertex j. If there is no edge between vertices i and j, then set SP[i][j] to infinity.

#     For each vertex k from 1 to n, compute the shortest path between every pair of vertices (i,j) that passes through k. To do this, update SP[i][j] as follows:

#     SP[i][j] = min(SP[i][j], SP[i][k] + SP[k][j])

#     This means that the shortest path from vertex i to vertex j that passes through k is the minimum of the current shortest path from i to j and the sum of the shortest path from i to k and the shortest path from k to j.

#     After the step 2 is complete, the SP array will contain the shortest path between every pair of vertices in the graph.

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



edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]

size = 8

import numpy as np

W = np.zeros(shape=(size,size,2))

for (i,j,w) in edges:

    W[i,j,0] = 1

    W[i,j,1] = w    

print(floydwarshall(W))