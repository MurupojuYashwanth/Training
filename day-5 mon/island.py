def mat(l,i,j,n):
    if j+1<n:
        if l[i][j+1]==1:
            l[i][j+1]=0
            mat(l,i,j+1,n)
    if i+1<n:
        if l[i+1][j]==1:
            l[i+1][j]=0
            mat(l,i+1,j,n)
    if i-1>=0:
        if l[i-1][j]==1:
            l[i-1][j]=0
            mat(l,i-1,j,n)
    if j-1>=0:
        if l[i][j-1]==1:
            l[i][j-1]=0
            mat(l,i,j-1,n)          
n=int(input())
l=[]
for i in range(n):
    x=[]
    for j in range(n):
        x.append(int(input()))
    l.append(x)
c=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c+=1
            mat(l,i,j,n)
print("count=",c)