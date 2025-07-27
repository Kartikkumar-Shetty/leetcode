class SuffixTrie:

    def __init__(self,s):

        self.root = {}

        s = s + "$"

        for i in range(len(s)):

            curr = self.root

            for c in s[i:]:

                if c not in curr.keys():

                    curr[c] = {}

                curr = curr[c]

    def followPath(self,s):

        curr = self.root

        for c in s:

            if c not in curr.keys():

                return(None)

            curr = curr[c]

        return(curr)

    def hasSuffix(self,s):

        node = self.followPath(s)

        return(node is not None and "$" in node.keys())

ST = SuffixTrie('card')

print(ST.root)

print(ST.followPath('a'))

print(ST.hasSuffix('aa'))