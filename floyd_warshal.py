def floyd_warshall(edges):
    mat = []
    max = 0
    infinity = float('inf') 
    for e in edges:
        if max<e[0]:
            max = e[0]
        if max<e[1]:
            max = e[1]
    for i in range(max+1):
        arr = []
        for j in range(max+1):
            arr.append(infinity)
        mat.append(arr)
    

    for e in edges:
        mat[e[0]][e[1]] = e[2]
    for k in range(max+1):
        for i in range(max+1):
            for j in range(max+1):
                if not i==j:
                    mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])
    print(mat)
    print("\n\n")
    return mat

# floyd_warshall([(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)])

def floyd_warshall_with_WL(WL):
    print(WL)
    mat = []
    max = 0
    for v1 in WL:
        for v2 in WL[v1]:
            if max<v2[0]:
                max = v2[0]
    
    infinity = float('inf')
    
    for i in range(max+1):
        arr = []
        for j in range(max+1):
            arr.append(infinity)
        mat.append(arr)
    
    for w in WL.keys():
        for i in WL[w]:
            mat[w][i[0]] = i[1]
    
    for k in range(max+1):
        for i in range(max+1):
            for j in range(max+1):
                if not i==j:
                    mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])
    print("\n\n")
    print(mat)
    total = 0
    for i in range(max+1):
        for j in range(max+1):
            if not mat[i][j] == infinity:
                total = total + mat[i][j]
    return total
    
    
floyd_warshall_with_WL({0: [(1, 10), (2, 50), (3, 300)], 1: [(0, 10), (2, 30), (6, 65), (3, 40)], 2: [(0, 50), (1, 30), (5, 76), (4, 20)], 3: [(0, 300), (1, 40), (4, 60)], 4: [(6, 37), (3, 60), (2, 20)], 5: [(6, 45), (2, 76)], 6: [(5, 45), (4, 37), (1, 65)]})