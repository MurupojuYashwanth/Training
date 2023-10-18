l=list(map(int,input().split()))
'''for i in range(len(l)):
    print(i,'=',l[i]*'x')'''
ma=max(l)
for i in range(ma,0,-1):
    print(i,'|',end=' ')
    for j in l:
        if j>=i:
            print('*',end='')
        else:
            print(' ',end='')
    print()