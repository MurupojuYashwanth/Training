def fun(n,st,end):
    if st<end:
        piv=qs(n,st,end)
        fun(n,st,pi-1)
        fun(n,pi+1,end)
n=list(map(int,input().split()))
#st,end=0,n-1
print(fun(n,0,len(n)-1))