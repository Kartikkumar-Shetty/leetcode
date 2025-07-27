    # Calculate the frequency of each character in the string.
    # Sort the characters in increasing order of the frequency.
    # Make each unique character as a leaf node.
    # Create an empty node z. Assign the minimum frequency to the left child of z and assign the second minimum frequency to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.
    # Remove these two minimum frequencies from Q and add the sum into the list of frequencies.
    # Insert node z into the tree.
    # Repeat steps 3 to 5 for all the characters.
    # For each non-leaf node, assign 0 to the left edge and 1 to the right edge.
    
    
class Node:

    def __init__(self,frequency,symbol = None,left = None,right = None):

        self.frequency = frequency

        self.symbol = symbol

        self.left = left

        self.right = right


# Solution        

        

def Huffman(s):

    huffcode = {}

    char = list(s)

    freqlist = []

    unique_char = set(char)

    for c in unique_char:

        freqlist.append((char.count(c),c))

    nodes = []

    for nd in sorted(freqlist):

        nodes.append((nd,Node(nd[0],nd[1])))

    while len(nodes) > 1:

        nodes.sort()

        L = nodes[0][1]

        R = nodes[1][1]

        newnode = Node(L.frequency + R.frequency, L.symbol + R.symbol,L,R)

        nodes.pop(0)

        nodes.pop(0)

        nodes.append(((L.frequency + R.frequency, L.symbol + R.symbol),newnode))


    for ch in unique_char:

        temp = newnode

        code = ''

        while ch != temp.symbol:           

            if ch in temp.left.symbol:

                code += '0'

                temp = temp.left

            else:

                code += '1'

                temp = temp.right

        huffcode[ch] = code   

    return huffcode




s = 'abbcaaaabbcdddeee'

res = Huffman(s)

for char in sorted(res):

    print(char,res[char])