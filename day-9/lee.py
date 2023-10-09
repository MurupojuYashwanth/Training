s=input()
s=sorted(s)
s="".join(s)
x=s[-1]+s[:len(s)-1]
print(x[::-1],type(x))
