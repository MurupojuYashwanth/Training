n=list(map(int,input().split()))
r=0
for i in n:
    r=r^i
print(r)