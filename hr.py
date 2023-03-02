
l2=[]
len2=0
if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        l1=[]
        l1.append(name)
        l1.append(score)
        l2.append(l1)
len2=len(l2)
l3=[]
l4=[]
for i in range(len2):
   l3.append(l2[i][1])
l3.sort()
for i in range(len2):
    if(l2[i][1]==l3[1]):
      l4.append(l2[i][0])
l4.sort()
len4=len(l4)
for i in range(len4):
   print(l4[i])