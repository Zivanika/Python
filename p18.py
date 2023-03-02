lst=eval(input("Enter a list: "))
l1=len(lst)
lst2=[]
count=0
for i in range(0,l1):
    for j in range(0,l1):
        if(lst[i]==lst[j]):
            count=count+1
            lst2[j]="visited"
    if(lst2[j]!="visited"):
        lst2[j]=count
for i in range(0,len(lst2)):
    if(lst2[i]!)
    print(arr[i]," ")