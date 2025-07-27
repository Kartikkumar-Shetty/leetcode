# Algorithm Steps

# Here are the step-by-step instructions for the Bellman-Ford algorithm:

#     Initialize the distance array: Set the distance of the source vertex to 0 and the distances of all other vertices to infinity.

#     Relax all edges: Repeat the following step (V-1) times, where V is the number of vertices in the graph. For each edge (u,v) with weight w, if the distance to u plus w is less than the distance to v, update the distance to v to the distance to u plus w.

#     Check for negative weight cycles: After relaxing all edges V-1 times, check for negative weight cycles. For each edge (u,v) with weight w, if the distance to u plus w is less than the distance to v, there exists a negative weight cycle.

#     Print the distance array: If there are no negative weight cycles, print the distance array, which contains the shortest path distances from the source vertex to all other vertices.


def bellmanfordlist(WList,s):

    # Initialization

    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])

    distance = {}

    for v in WList.keys():

        distance[v] = infinity        

    distance[s] = 0

    

    # Computing shortest distance for each vertex from source

    # Repeat the process n times where n is number of vertices   

    for i in WList.keys():

        # Check for each adjacent of u vertex

        for u in WList.keys():

            for (v,d) in WList[u]:

                # If distance of v through u is smaller than the current distance of v, then update

                if distance[u] + d < distance[v]:

                    distance[v] = distance[u] + d

    return(distance)



edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]

size = 8

WL = {}

for i in range(size):

    WL[i] = []

for (i,j,d) in edges:

    WL[i].append((j,d))

print(bellmanfordlist(WL,0))