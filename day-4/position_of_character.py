n=input()
if n>='A' and n<='Z':
    print(ord(n)-64)
elif n>='a' and n<='z':
    print(ord(n)-96)
else:
    print("Enter a valid alphabet")