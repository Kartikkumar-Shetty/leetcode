class Stack:
    arr = []
    def __init__(self):
        self.arr = []
    
    def push(self, data):
        self.arr.append(data)
        
    def pop(self):
        if len(self.arr)==0:
            return None
        return self.arr.pop()

def decode(root, ciphertext):
    symbol_table = {}
    stk = Stack()
    calculate_code(root, symbol_table, stk)
    print(symbol_table)
    
def calculate_code(root, symbol_table, stk):
    if root.left == None and root.right == None:
        symbol_table[stk.arr] = root.symbol
    
    if not root.left == None:
        stk.push(0)
        calculate_code(root.left, symbol_table, stk)
        stk.pop()
    
    if not root.right == None:
        stk.push(1)
        calculate_code(root.right, symbol_table, stk)
        stk.pop()
        