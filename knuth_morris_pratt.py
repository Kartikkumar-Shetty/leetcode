def kmp_fail(p):

    m = len(p)

    fail = [0 for i in range(m)]

    j,k = 1,0

    while j < m:

        if p[j] == p[k]:

            fail[j] = k+1

            j,k = j+1,k+1

        elif k > 0:

            k = fail[k-1]

        else:

            j = j+1

    return(fail)


def find_kmp(t, p):

    match =[]

    n,m = len(t),len(p)

    if m == 0:

        match.append(0)

    fail = kmp_fail(p)

    j = 0

    k = 0

    while j < n:

        if t[j] == p[k]:

            if k == m - 1:

                match.append(j - m + 1)

                k = 0

                j = j - m + 2

            else:

                j,k = j+1,k+1

        elif k > 0:

            k = fail[k-1]

        else:

            j = j+1

    return(match)

print(find_kmp('ababaabbaba','aba'))