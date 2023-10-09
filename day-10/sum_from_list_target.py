def fun(l,st,en,t):
    while st<en:
        if l[st]+l[en]==t:
            return [st,en]
            break
        elif l[st]+l[en]>t:
            en-=1
        elif l[st]+l[en]<t:
            st+=1
    return -1
l=list(map(int,input().split()))
t=int(input())
st,en=0,len(l)-1
print(fun(l,st,en,t))
