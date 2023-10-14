s1=input()
s2=input()
subs=""
for i in range(len(s2)):
    s=""
    for j in range(i,len(s2)):
        s+=s2[j]
        if s in s1 and len(subs)<len(s):
            subs=s
print(subs)