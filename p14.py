sen1=input("Enter a sentence:")
sub1=input("Enter a substring:")
count=0
l1=sen1.split(" ")
print(l1)
len1=len(l1)
for i in range(0,len1):
    if(l1[i]==sub1):
        count=count+1
print("The number of occurances of ",sub1," is: ",count)