x=int(input("Enter a number: "))
match x:
    case 0:
          print("x is 0")
    case :
         print("x is 2")
    case _ if x!=10:
                    print("x is not equal to 10")
    case _ if x==10:
                   print("x is equal to 10")
    case _:
            print("Default")