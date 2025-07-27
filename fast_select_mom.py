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




def fastselect(L,l,r,k): # k-th smallest in L[l:r]

  if (k < 1) or (k > r-l):

    return(None)


  # Find MoM pivot and move to L[l]

  pivot = MoM(L[l:r])

  pivotpos = min([i for i in range(l,r) if L[i] == pivot])

  (L[l],L[pivotpos]) = (L[pivotpos],L[l])


  (pivot,lower,upper) = (L[l],l+1,l+1)

  for i in range(l+1,r):

    if L[i] > pivot:  # Extend upper segment

      upper = upper + 1

    else: # Exchange L[i] with start of upper segment

      (L[i], L[lower]) = (L[lower], L[i])

      (lower,upper) = (lower+1,upper+1)

  (L[l],L[lower-1]) = (L[lower-1],L[l]) # Move pivot

  lower = lower - 1

  

  # Recursive calls

  lowerlen = lower - l

  if k <= lowerlen:

    return(fastselect(L,l,lower,k))

  elif k == (lowerlen + 1):

    return(L[lower])

  else:

    return(fastselect(L,lower+1,r,k-(lowerlen+1)))

print(fastselect([4,3,5,6,2,1,8,9,7,10,13,15,18,17,11],0,15,4))