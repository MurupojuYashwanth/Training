n=list(map(int,input().split()))
c=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]<n[j]:
            c+=1
print(c)