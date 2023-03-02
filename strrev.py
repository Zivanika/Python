str1=input("Enter a string: ")
l1=len(str1)
print("The string in reverse order is:")
for i in range(-1,(-l1-1),-1):
    print(str1[i])

print(str1[-1:-l1:-1])