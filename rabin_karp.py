def rabinkarp(t,p):

    poslist = []

    numt,nump = 0,0

    for i in range(len(p)):

        numt = 10*numt + int(t[i])

        nump = 10*nump + int(p[i])

    if numt == nump:

        poslist.append(0)

    for i in range(1,len(t)-len(p)+1):

        numt = numt - int(t[i-1])*(10**(len(p)-1))

        numt = 10*numt + int(t[i+len(p)-1])

        if numt == nump:

            poslist.append(i)

    return(poslist)

print(rabinkarp('233323233454323','23'))