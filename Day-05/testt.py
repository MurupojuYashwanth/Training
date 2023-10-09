mat = [[1,0],[1,0],[1,0],[1,1]]
l=[]
k=4
x=[]
for i in mat:
    l.append(i.count(1))
#print(l)
a=l.copy()
a.sort()
print(a)
print(l)
for i in range(len(l)):
    for j in range(len(l)):
        if a[i]==l[j]:
            x.append(j)
print(x[:k])
            
'''
a={}
for i in range(len(l)):
    a[i]=l[i]
print(a)
'''