n=input()
k=int(input())
if k>len(n):
    x=k%len(n)
    print((n*(k//len(n)))+n[:x])
else:
    print(n[:k])