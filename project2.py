print("welcome to the pattern generator and number analyzer!\n")

while True:
    print("select an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of nubers")
    print("3. Exit")

    choice=input("Enter your choice: ")
    print()

    if choice == '1':
        rows=int(input("Enter the number of rows for the pattern: "))
        print("\npattern")
        for i in range (1, rows + 1):
            print("*" * i)
        print()
    elif choice == '2':
        start= int(input("Enter the start of the range: "))
        end= int(input("Enter the and of the range: "))

        total_sum=0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"number {num} is even")
            else:
                print(f"number {num} is odd")

            total_sum += num 

        print(f"sum of all number from {start} to {end} is: {total_sum}")
        print()

    elif choice == '3':
        print("Enter the program. goodbye!")
        break 
    else:
        print("Invalid choice! please select 1, 2, or 3.\n")
