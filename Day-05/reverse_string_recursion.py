'''def rev(s):
    x=len(s)
    for i in range(x//2):
        if s[i]!=s[x-i-1]:
            return False
        return True
        '''

def rev(s,i,j):
    if i<j:
        if s[i]!=s[j]:
            return False
        return rev(s,i+1,j-1)
    return True
s=input()
i=0
j=len(s)-1
print(rev(s,i,j))
