a=int(input())
b=int(input())
c=int(input())

print("The Maximum is",end="")
if b<= a >=c:
    print(a)
elif a<= b >=c:
    print(b)
elif a<= c >=b:
    print(c)