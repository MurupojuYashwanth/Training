def fun(l,t):
    i=0
    j=i+1
    s=l[i]+l[j]
    while i<len(l) and j<len(l)-1:
        if s==t:
            return l[i:j+1]
        elif s<t:
            j+=1
            s+=l[j]
        elif s>t:
            s-=l[i]
            i+=1
l=list(map(int,input().split()))
t=int(input())
print(fun(l,t))
#algomonster