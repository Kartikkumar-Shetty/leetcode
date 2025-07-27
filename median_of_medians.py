def MoM(L): # Median of medians

  if len(L) <= 5:

    L.sort()

    return(L[len(L)//2])

  # Construct list of block medians

  M = []

  for i in range(0,len(L),5):

    X = L[i:i+5]

    X.sort()

    M.append(X[len(X)//2])

  return(MoM(M))

print(MoM([4,3,5,6,2,1,8,9,7,10,13,15,18,17,11]))