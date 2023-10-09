n=input()
k=int(input())
if n>='A' and n<='Z':
    print(chr(64+((ord(n)-64)+k)%26))
elif n>='a' and n<='z':
    print(chr(96+((ord(n)-96)+k)%26))