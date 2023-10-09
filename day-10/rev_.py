def fun(l,st,en):
    while(st<en):
        l[st],l[en]=l[en],l[st]
        st+=1
        en-=1
    return l
l=list(map(int,input().split()))
#t=int(input())
print(fun(l,0,len(l)-1))