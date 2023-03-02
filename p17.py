l=[1,3,5,1,6,7,1]
len1=len(l)
count=0
for i in range(0,len1):
    if l[i]==1 and count<=3:
        count=count+1
print(l[i-1])