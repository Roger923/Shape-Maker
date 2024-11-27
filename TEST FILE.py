print("Welcome to Shape Maker by Roger_923")
print()
input("Press enter to continue...")
print()
while True:
    try:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        symbol = input("Enter a symbol to use: ")
    except:
        print("Try Again!")
        continue

    else:
        for i in range(rows):
            for j in range(columns):
                print(symbol, end="")
            print()

        choice = input("Do you want to continue(yes/no): ")

        if choice == "no":
            break

        else:
            continue
