
def fun(n,st,end):
    if st<end:
        mid=(st+end)//2
        print(n[st:mid+1])
        print(n[mid+1:end+1])
        fun(n,st,mid)
        fun(n,mid+1,end)
        #if st!=end:
            
n=list(map(int,input().split()))
fun(n,0,len(n)-1)
