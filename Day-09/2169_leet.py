n1,n2=map(int,input().split())
c=0
while n1>0 and n2>0:
    if n1<n2:
        n2=n2-n1
    elif n1>n2:
        n1=n1-n2
    else:
        n1=n1-n2
    c+=1
print(c)