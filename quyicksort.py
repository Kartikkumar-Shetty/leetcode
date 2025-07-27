def partition(L,lower,upper):

  # Select first element as a pivot 

  pivot = L[lower]

  i = lower

  for j in range(lower+1,upper+1):

    if L[j] <= pivot:

      i += 1

      L[i],L[j] = L[j],L[i]

  L[lower],L[i]= L[i],L[lower]

  # Return the position of pivot

  return i


def quicksort(L,lower,upper):

  if(lower < upper):

    pivot_pos = partition(L,lower,upper);

    # Call the quick sort on leftside part of pivot

    quicksort(L,lower,pivot_pos-1)

    # Call the quick sort on rightside part of pivot

    quicksort(L,pivot_pos+1,upper)

  return L