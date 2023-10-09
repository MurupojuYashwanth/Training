def rev(s):
    r=""
    for i in s:
        r=i+r
    if s==r:
        return True
    else:
        return False 
s=input()
print(rev(s))