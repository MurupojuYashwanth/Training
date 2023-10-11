def fun(l):
    le=0
    r=len(l)-1
    i=0
    while i<=r:
        if l[i]==0:
            l[i],l[le]=l[le],l[i]
            le+=1
            i+=1
        elif l[i]==1:
            i+=1
        elif l[i]==2:
            l[i],l[r]=l[r],l[i]
            r-=1
    return l
l=list(map(int,input().split()))
print(fun(l))