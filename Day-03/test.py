 
'''
n=bin(int(input()))[2:]
c=0
for i in str(l):
    if i=='1':
        c+=1
if c==1:
    print("true")
else:
    print("false")
print(c)
''
n=int(input())
print(n|n+1)
'''
'''
n=str(bin(int(input()))[2:])
k=int(input())
n=n[::-1]
if n[k]=='1':
    print("true")
else:
    print("false")
    '''
n,k=map(int,input().split())
