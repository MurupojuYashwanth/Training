s1=input()
x=1
subs=""
l=len(s1)
if l==0:
    print(0)
elif l==1:
    print(1)
s=""
for i in range(l):
    if s1[i] not in s:
        s+=s1[i]
    else:
        if x<len(s):
            x=len(s)
        #print(s)
        s=""
        s+=s1[i]
print(x)
