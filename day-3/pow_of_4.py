n=int(input())
c=0
while n:
    if n&(n-1)==0:
        c+=1
    else:
        break
    n=n>>1
print("yes" if c&1 else "false")

