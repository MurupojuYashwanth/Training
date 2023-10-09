c=int(input())
wt=list(map(int,input().split()))
p=list(map(int,input().split()))
'''
#print(list(l))
x=[]
for i in range(len(wt)):
    x.append(p[i]/wt[i])
    '''
l=list(zip(wt,p))
l.sort(key=lambda y:y[1]/y[0],reverse=True)
#l.sort(key=lambda y:y[2],reverse=True)
print(l)
maxpr=0
for weight,pro in l:
    if weight<c:
        maxpr+=pro
        c-=weight
    else:
        maxpr+=c*(pro/weight)
        break
print(maxpr)