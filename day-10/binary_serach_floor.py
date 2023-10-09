import math
def fun(l,st,en,se):
    mid=(st+en)//2
    if se==l[mid]:
        return True
    elif st==en:
        return l[st]
    elif se<l[mid]:
        return fun(l,st,mid-1,se)
    elif se>l[mid]:
        return fun(l,mid+1,en,se)
    #return math      
l=list(map(int,input().split()))
n=int(input())
print(fun(l,0,len(l)-1,n))