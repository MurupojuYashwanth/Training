def fun(x):
    if x==0:
        return 0
    fun(x-1)
    print(x)
n=int(input())
fun(n)