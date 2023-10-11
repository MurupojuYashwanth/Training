def result(le,ri):
    x=[]
    i,j=0,0
    while i<len(le) and j<len(ri):
        if le[i]<ri[j]:
            x.append(le[i])
            i+=1
        else:
            x.append(ri[j])
            j+=1
    x.extend(le[i:])
    x.extend(ri[j:])
    return x
def merge(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    le=l[:mid]
    ri=l[mid:]
    le=merge(le)
    ri=merge(ri)
    r=result(le,ri)
    return r   
l=list(map(int,input().split()))
print(merge(l))