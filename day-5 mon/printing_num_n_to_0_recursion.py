def fun(x):
    if x==0:
        return 0
    print(x)
    return fun(x-1)
n=int(input())
print(fun(n))
