if __name__ == '__main__':
    n = int(input())
    a=n+1
    s=0
    # if(1<=n<=9):
    #  for i in range(1,a):
    #     s+=i*10**(n-1)
    #     n=n-1
    if(10<=n<=90):
        for i in range(1,a):
            s+=i*(10**(n))
            n=n-1

    print(s)
        