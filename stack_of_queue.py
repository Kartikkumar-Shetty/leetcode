class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, key):
        self.items.insert(0,key)
    def dequeue(self):
        return self.items.pop()
            
class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0
    def push(self,data):
        s = self.size
        while s>0:
            d = self.q1.dequeue()
            self.q2.enqueue(d)
            s=s-1
        
        self.q1.enqueue(data)
        
        s = self.size
        while s>0:
            d = self.q2.dequeue()
            self.q1.enqueue(d)
            s=s-1
        self.size = self.size + 1

    def pop(self):
        if self.size == 0:
            return "Stack is empty"
        self.size = self.size - 1
        return self.q1.dequeue()

    def top(self):
        data = self.q1.dequeue()
        s = self.size-1
        while s>0:
            d = self.q1.dequeue()
            self.q2.enqueue(d)
            s=s-1
        self.q1.enqueue(data)
        
        s = self.size-1
        while s>0:
            d = self.q2.dequeue()
            self.q1.enqueue(d)
            s=s-1
        return data
        
    def isempty(self):
        if self.size == 0:
            return True
        return False


inp = [10,20,30,40,50]
dl = 2
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())