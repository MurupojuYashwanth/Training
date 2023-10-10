def fun(n,st,en):
    mid=(st+en)/2
    if int(mid*mid)==n:
        return int(mid)
    elif int(mid*mid)<n:
        return fun(n,mid+1,en)
    elif int(mid*mid)>n:
        return fun(n,st,mid-1)
n=int(input())
print(fun(n,1,n//2))