sen1=input("Enter a sentence: ")
lc=uc=0
dc=0
l1=len(sen1)
for i in sen1:
    if(i.isupper()):
        uc=uc+1
    if(i.islower()):
        lc=lc+1
    if(i.isdigit()):
        dc=dc+1
print("Number of uppercase letters: ",uc)
print("Number of lowercase letters: ",lc)
print("Number of digits: ",dc)
print("Number of alphabets: ",lc+uc)
