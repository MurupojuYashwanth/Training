def qsort(n,st,end):
    pi=n[end]
    i=st-1
    for j in range(st,end):
        if n[j]<pi:
            i=i+1
            n[j],n[i]=n[i],n[j]
    n[i+1],n[end]=n[end],n[i+1]
    return i+1
def quick(n,st,end):
n=list(map(int,input().split()))
