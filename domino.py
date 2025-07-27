size = 4
mat = []
s_row1 = "8 6 2 3".split(" ")
s_row2 = "9 7 1 2".split(" ")

arr = []
print(s_row1)
print(s_row2)
for i in s_row1:
    if i == "":
        continue
    arr.append(int(i))
mat.append(arr)

arr = []
for i in s_row2:
    if i == "":
        continue    
    arr.append(int(i))
mat.append(arr)

i,j=0,0

def calculate_max_score(mat,i,j,memo):
    if f"{i}-{j}" in memo:
        return memo[f"{i}-{j}"]
    score,score1,score2 = 0,0,0
    print(f"calling wiith - i:{i},j:{j}")
    if j+1<=len(mat[0])-1:
        print(f"calculating score 1 with {i},{j}")
        score1 = abs(mat[i][j]-mat[i][j+1])
        score1 = score1+abs(mat[i+1][j]-mat[i+1][j+1])
    if j+2<=len(mat[0])-1:
        score1 = score1 + calculate_max_score(mat,i,j+2, memo)
    
    print(f"calculating score 2 with {i},{j}")
    score2 = abs(mat[i][j]-mat[i+1][j])
    if j+1<=len(mat[0])-1:
        score2 = score2 + calculate_max_score(mat,i,j+1, memo)
    score = max(score1,score2)
    memo[f"{i}-{j}"] = score
    
    return score

memo = {}      
print(calculate_max_score(mat,0,0,memo))
