conc = "t"
while conc == "t":
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter ur choice(1/2/3/4:):"))  # choice selection

    if choice == 1:
        n1 = eval(input("Enter 1st no:"))  # input first number
        n2 = eval(input("Enter 2st no:"))  # input second number
        print(n1 + n2)

    # subtraction
    elif choice == 2:
        n1 = eval(input("Enter 1st no:"))  # input first number
        n2 = eval(input("Enter 2st no:"))  # input second number
        print(n1 - n2)

    # multiplication
    elif choice == 3:
        n1 = eval(input("Enter 1st no:"))  # input first number
        n2 = eval(input("Enter 2st no:"))  # input second number
        print(n1 * n2)

    #  division
    elif choice == 4:
        n1 = eval(input("Enter 1st no:"))  # input first number
        n2 = eval(input("Enter 2st no:"))  # input second number
        print(n1 / n2)

    # invalid input
    else:
        print("Invalid input")
    con = input("Do you want to continue calculation? (Y/N):")
    if con == "Y" or con == "y":
        continue
    else:
        break
