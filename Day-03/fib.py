def fi(n):
    if n<=1:
        return n
    else:
        return fi(n-1)+fi(n-2)
n=int(input())
#for i in range(n):
 #   print(fi(i),end=" ")
print(fi(n))
