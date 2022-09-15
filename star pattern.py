try:
    print("Enter the number of rows")
    n1 = int(input())
    n2 = int(input("Enter 0 or 1\n"))
    n4 = bool(n2)
    n3 = 1
    if n4 == True:
        while n1 >= n3:
            print("*" * n3, end="\n", )
            print(end="")
            n3 = n3 + 1

    if n4 == False:
        while n3 <= n1:
            print("*" * n1, end="")
            print("\n", end="")
            n1 = n1 - 1

except Exception as e:
    print(e)
    print("Invalid input!")
