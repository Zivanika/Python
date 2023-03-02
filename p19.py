a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
m=(a-3)//2
m1=m-2
n=1
for i in range(0,a//2):
    print("-"*m,".|."*n,"-"*m)
    m=m-3
    n=n+2

print("-"*m1,"WELCOME","-"*m1)
