digits=input()
d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
if len(digits)<=0:
    print("[]")
elif len(digits)==1:
    r=[]
    for i in d[digits[0]]:
        r.append(i)
    print(r)
elif len(digits)==2:
    r=[]
    for i in d[digits[0]]:
        for j in d[digits[1]]:
            r.append(i+j)
    print(r)
elif len(digits)==3:
    r=[]
    for i in d[digits[0]]:
        for j in d[digits[1]]:
            for k in d[digits[2]]:
                r.append(i+j+k)
    print(r)
else:
    r=[]
    for i in d[digits[0]]:
        for j in d[digits[1]]:
            for k in d[digits[2]]:
                for l in d[digits[3]]:
                    r.append(i+j+k+l)
    print(r)