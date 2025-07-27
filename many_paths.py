class Stack:
    arr = []
    def __init__(self):
        self.arr = []
        
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        if len(self.arr)==0:
            return None
        return self.arr.pop()
    def get_arr(self):
        return self.arr
    def exists(self, data):
        return data in self.arr
        

def backandforth(AList, end1, end2):    
    path = []
    visited = Stack()
    stk = Stack()
    paths = []
    stk.push(end1)
    Dfs(AList, end1, end2, stk,visited, paths)
    print(paths)

def Dfs(AList, end1, end2, stk,visited ,paths):
    #print(stk.arr)
    for i in AList[end1]:
        if visited.exists(i):
            continue
        #print(i," in ", end1)
        if i == end2:
            paths.append(stk.get_arr())
            #print("found")
            return
        stk.push(i)
        visited.push(i)
        print(stk.arr)
        Dfs(AList, i, end2, stk,visited, paths)
        stk.pop()

end1 = int(input())
end2 = int(input())

AList = {}

while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
        AList[u].append(v)

print(backandforth(AList, end1, end2))