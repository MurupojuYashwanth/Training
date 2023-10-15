l=list(map(int,input().split()))
k=int(input())
k=k%len(l)
#x=l[k-1:]+l[:k-1]
#x=l[k:]+l[:k]

x=l[-k:]+l[:len(l)-k]
print(x)