n=list(map(int,input().split()))
for i in range(1,len(n)):
    for j in range(len(n)-i):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)