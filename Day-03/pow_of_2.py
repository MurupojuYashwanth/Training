n=int(input())
print("true" if n&(n-1)==0 else "false")

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
'''