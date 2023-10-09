l=list(map(int,input().split()))
l.sort()
print(l)
s=[]
for i in range(len(l)):
    #print(i)
    if i^l[i-1]!=0:
        s.append(i)
    else:
        continue
print(s)