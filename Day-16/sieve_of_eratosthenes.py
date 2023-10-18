def fun(n):
    l=[1 for i in range(n+1)]
    for i in range(2,n+1):
        k=i
        if l[i]==1:
            k+=i
            while k<=n:
                l[k]=0
                k+=i
    return [i for i in range(2,n+1) if l[i]==1]          
n=int(input())
print(fun(n))