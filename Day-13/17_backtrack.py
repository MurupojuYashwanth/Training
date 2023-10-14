res=[]
def backtrack(i,curstr):
    if(len(digits)==len(curstr)):
        res.append(curstr)
        return
        for c in d[digits[i]]:
            backtrack(i+1,curstr+c)
    if digits:
        backtrack(0,"")
    return res