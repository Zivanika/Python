lst=eval(input("Enter a list(1 to 12): "))
l1=len(lst)
for i in range(0,l1):
    if(lst[i]>10):
        lst[i]=10
print(lst)