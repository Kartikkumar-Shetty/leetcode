class Queue:
    arr = []
    def __init__(self):
        self.arr = []
    def enqueue(self,data):
        self.arr.append(data)
    def dequeue(self):
        if len(self.arr) == 0:
            return None
        data = self.arr[0]
        self.arr = self.arr[1:len(self.arr)]
        return data
    def exists(self):
        return (len(self.arr)>0)

def minimumhops(AList, start, end):
    visited = {}
    q = Queue()
    q.enqueue((start,[]))
    path = []
    while q.exists():
        n = q.dequeue()
        for i in AList[n[0]]:
            if i in visited:
                continue
            if i == end:
                n[1].append(i)
                path = n[1]
                break
            child = (i,n[1]+[n[0]])
            q.enqueue(child)
            visited[i]=True
    print(path)    
    return path
        

start = 8
end = 0
AList = {0: [8], 8: [9], 1: [3, 5, 8], 3: [1, 7, 2], 5: [4], 2: [8, 9], 9: [1], 7: [8], 4: [2, 6], 6: [9]}
shortestpath = minimumhops(AList, start, end)
print(len(shortestpath))