def island(l,i,j,n):
    if i+1<n and l[i+1][j] == 1:
        l[i+1][j] = 2
        island(l, i + 1, j, n)
    if i-1>=0 and l[i-1][j] == 1:
        l[i - 1][j] = 2
        island(l, i - 1, j, n)
    if j + 1 < n and l[i][j + 1] == 1:
        l[i][j + 1] = 2
        island(l, i, j + 1, n)
    if j - 1 >= 0 and l[i][j - 1] == 1:
        l[i][j - 1] = 2
        island(l, i, j - 1, n)
n=int(input())
l=[]
for i in range(n):
    x=[]
    for j in range(n):
        x.append(int(input()))
    l.append(x)
sr,sc=map(int,input().split())
print(l)
c=0
for i in range(n):
    for j in range(n):
        if l[sr][sc]==1:
            c+=1
            island(l,i,j,n)
for i in l:
    print(i)
            
