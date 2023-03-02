def swap_case(s):
    str1=""
    for i in s:
        if i.islower():
            str1+=i.upper()
        elif i.isupper():
            str1+=i.lower()
        else:
            str1+=i
    return str1

s1=input("Enter a string: ")
result=swap_case(s1)
print(result)