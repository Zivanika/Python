def swap_case(s):
    l1=len(s)
    newStr=""
    for i in range(0,l1):
        if s[i].islower:
            newStr +=s[i].upper
        elif s[i].isupper:
            newStr +=s[i].lower
        else:
            newStr +=s[i]
    return newStr
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)