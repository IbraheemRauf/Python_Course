x = int(input("Enter the value of x:"))
match x:
    case 0:
        print("so x is zero")
    case 4:
        print("so x is four")
    case _:
        print(x)        