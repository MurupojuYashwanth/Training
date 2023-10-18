def fun(l,t):
    #i=0
    #j=i+1
    for i in range(len(l)):
        j=i+1
        if sum(l[i:j+1])==t:
            return l[i:j+1]
        elif sum(l[i:j+1])<t:
            j+=1
        elif sum(l[i:j+1])>t:
            i+=1
l=list(map(int,input().split()))
t=int(input())
print(fun(l,t))