# Algorithm Steps

# Here are the steps for the of Kruskal's algorithm:

#     Sort all the edges of the graph in non-decreasing order of their weights.

#     Create a new empty set for the minimum spanning tree (MST).

#     Iterate through the sorted edges, starting with the edge with the smallest weight.

#     For each edge, check if adding it to the MST will create a cycle. 

#     If the edge does not create a cycle, add it to the MST.

#     Repeat steps 4 and 5 until all vertices are included in the MST, or until the desired number of edges have been added.

#     Return the MST.

def kruskal(WList):

    # Initialization

    (edges,component,TE) = ([],{},[])

    for u in WList.keys():

        # Weight as first value in tuple to sort easily

        edges.extend([(d,u,v) for (v,d) in WList[u]])

        # Initially each vertex as single components and assign leader of each component 

        component[u] = u

    

    # Sort the edges in increasing order of their weights

    edges.sort()

   

    for (d,u,v) in edges:

        # If (u,v) edge is not creating the cycle in MST, add the edge in MST

        if component[u] != component[v]:

            TE.append((u,v))

            c = component[u]

            # Update of component leader 

            for w in WList.keys():

                if component[w] == c:

                    component[w] = component[v]

    return(TE)



dedges = [(0,1,10),(0,2,18),(1,2,6),(1,4,20),(2,3,70),(4,5,10),(4,6,10),(5,6,5)]

edges = dedges + [(j,i,w) for (i,j,w) in dedges]

size = 7

WL = {}

for i in range(size):

    WL[i] = []

for (i,j,d) in edges:

    WL[i].append((j,d))

print(kruskal(WL))