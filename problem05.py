def simplecalc():
    a = int(input("enter the first number :"))
    b = int(input("enter the second number :"))

    print("enter 1 for sum")
    print("enter 2 for sub")
    print("enter 3 for mul")
    print("enter 4 for div")
    c=int(input("enter the number from 1 to 4: "))
    l = [1, 2, 3, 4]
    if c in l :
        print("out of sylebuss")

        if c==1 :
            print(a+b)
        elif c==2 :
            print(a-b)
        elif c==3 :
            print(b*a)
        elif c==4 :
            print("a/b")
    else:
        print("not valid number")
simplecalc()