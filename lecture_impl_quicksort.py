def quicksort(L,l,r): # Sort L[l:r]

    if (r - l <= 1):

        return L

    (pivot,lower,upper) = (L[l],l+1,l+1)

    for i in range(l+1,r):

        if L[i] > pivot:

            # Extend upper segment

            upper = upper+1

        else:

            # Exchange L[i] with start of upper segment

            (L[i], L[lower]) = (L[lower], L[i])

            # Shift both segments

            (lower,upper) = (lower+1,upper+1)

    # Move pivot between lower and upper

    (L[l],L[lower-1]) = (L[lower-1],L[l])

    lower = lower-1

    

    # Recursive calls

    quicksort(L,l,lower)

    quicksort(L,lower+1,upper)

    return(L)