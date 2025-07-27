class min_heap:

    def __init__(self,nodes):

        self.nodes = nodes

        self.size =len(nodes)

        self.create_min_heap()

    

    def isempty(self):

        return len(self.nodes) == 0

    

    def min_heapify(self,s):

        l = 2*s + 1

        r = 2*s + 2

        small = s

        if l<self.size and self.nodes[l][0][0] < self.nodes[small][0][0]:

            small = l

        if r<self.size and self.nodes[r][0][0] < self.nodes[small][0][0]:

            small = r

        if small != s:

            self.nodes[small],self.nodes[s] = self.nodes[s],self.nodes[small]

            self.min_heapify(small)


    def create_min_heap(self):

        for i in range((self.size//2)-1,-1,-1):

            self.min_heapify(i)

    

    def insert_min(self,v):

        self.nodes.append(v)

        self.size += 1

        index = self.size -1

        while(index > 0):

            parent = (index-1)//2

            if self.nodes[parent][0][0] > self.nodes[index][0][0]:

                self.nodes[parent],self.nodes[index] = self.nodes[index],self.nodes[parent]

                index = parent

            else:

                break

        pass

    

    def del_minheap(self):

        item = None

        if self.isempty():

            return item

        self.nodes[0],self.nodes[-1] = self.nodes[-1],self.nodes[0]

        item = self.nodes.pop()

        self.size -= 1

        self.min_heapify(0)

        return item


class Node:

    def __init__(self,frequency,symbol = None,left = None,right=None):

        self.frequency = frequency

        self.symbol = symbol

        self.left = left

        self.right = right


def Huffman(s):

    freqlist = []

    huffcode = {}

    char = list(s)

    unique_char = set(char)

    for c in unique_char:

        freqlist.append((char.count(c),c))

    nodes = []

    for nd in sorted(freqlist):

        nodes.append((nd,(Node(nd[0],nd[1]))))

    minheap_nodes = min_heap(nodes)


    while(minheap_nodes.size > 1):

        

        L = minheap_nodes.del_minheap()[1]

        R = minheap_nodes.del_minheap()[1]

        newnode = Node(L.frequency+R.frequency,L.symbol+R.symbol,L,R)

        internal_node = tuple(((L.frequency+R.frequency,L.symbol+R.symbol),newnode))

        minheap_nodes.insert_min(internal_node)


    for ch in unique_char:

        temp = newnode

        code = ''

        while ch!=temp.symbol:

            if ch in temp.left.symbol:

                code += '0'

                temp = temp.left

            else:

                code+= '1'

                temp = temp.right

        huffcode[ch] = code

    return huffcode 



s = 'abbcaaaabbcdddeee'

res = Huffman(s)

for char in sorted(res):

    print(char,res[char])