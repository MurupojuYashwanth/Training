import collections
st=collections.deque()
l=[5,4,3,2,1]
for i in l:
    st.append(i)
#print(st)
st.pop()
print(st)