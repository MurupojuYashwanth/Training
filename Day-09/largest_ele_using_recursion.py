n=list(map(int,input().split()))
def s(si,ei):
    if si==ei:
        return n[si]
    if si<ei:
        mid=(si+ei)//2
        return max(s(si,mid),s(mid+1,ei))
print(s(0,len(n)-1))