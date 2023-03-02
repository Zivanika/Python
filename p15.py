str1=input("Enter first string: ")
str2=input("Enter second string: ")
l1=len(str1)
l2=len(str2)
a1=l1
a2=l2
l2=len(str2)
i=j=0
if(l1>l2):
    print(str2)
    for i in range(0,l1//2):
        print(" "*i,str1[i],"  "*a1,str1[a1-1])
        a1=a1-1
    
else:
    print(str1,str2)
    for i in range(0,l2//2):
        print("  "*i,str2[i],"  "*a2,str2[a2-1])
        a2=a2-1
   
