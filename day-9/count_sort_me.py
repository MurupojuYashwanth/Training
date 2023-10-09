n=list(map(int,input().split()))
ma,mi=max(n),min(n)
print(ma,mi)
l=[0 for i in range(ma+1)]
x=[]
for i in range(len(n)):
    x.append(0)
print(l)
for i in n:
    l[i]=n.count(i)
print(l)
cu=[]
s=0
for i in range(len(l)):
    s+=l[i]
    cu.append(s)
print(cu)
for i in range(len(n)):
    x[cu[n[i]]-1]=n[i]
    cu[n[i]]-=1
print(x)