def fun(l,st,en):
    while(st<en):
        mid=(st+en)//2
        if l[mid]>l[mid+1] and l[mid]>l[mid-1]:
            en=mid
            return l[mid]
        else:
            st=mid+1
            #return fun(l,st,en)
l=list(map(int,input().split()))
print(fun(l,0,len(l)-1))