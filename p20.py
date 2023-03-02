lA=eval(input("Enter list A: "))
lB=eval(input("Enter list B: "))
leA=len(lA)
leB=len(lB)
for i in range(leA):
    ele=lA[i]
    if ele in lB:
        print("Overlapped")
        break
    else:
        print("Separated")