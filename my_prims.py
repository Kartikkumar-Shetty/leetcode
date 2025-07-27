def findRedundantEdges(E,n):
    visited = {}
    edges=[]
    distance={}
    max = 0
    visited_edges = {}
    for i in range(n):
        visited[i] = False
    for i in E:
        visited_edges[i] = False
        if max<i[2]:
            max = i[2]
        
    visited[0] = True
    distance[0] = 0
    for j in range(n):
        min_dist = max+1
        next_e = ""
        for i in E:
            if ((visited[i[0]] and not visited[i[1]]) or (not visited[i[0]] and visited[i[1]])) and i[2]<min_dist:
                next_e = i
                min_dist = i[2]

        if next_e == "":
            break
        visited_edges[next_e] = True
        edges.append(next_e)
        visited[next_e[0]] = True
        visited[next_e[1]] = True
    unvisited_edges = []
    for i in visited_edges.keys():
        if not visited_edges[i]:
            unvisited_edges.append(i)
    return unvisited_edges


n = 7
E=[(0,1,10),(0,2,50),(0,3,60),(5,6,75),(2,1,80),(6,4,90),(1,6,100),(2,5,110),(1,3,150),(3,4,180),(2,4,200)]
print(findRedundantEdges(E,n))