print("=== WELCOME TO THE PYTHON ESSENTIALS CALCULATOR ===")
while True:
    print("\nSelect an operation: ")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = int(input("Enter your operation you want to perform (1-5): "))

    if choice == 5:
        print("Thank you for using the calculator, goodbye!")
        break

    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        num1 = int(input("Enter First Interger Number: "))
        num2 = int(input("Enter second Integer Number: "))

        if choice == 1:
            print(f"Result of {num1} + {num2} is {num1+num2}")
        elif choice == 2:
            print(f"Result of {num1} - {num2} is {num1-num2}")
        elif choice == 3:
            print(f"Result of {num1} * {num2} is {num1*num2}")
        elif choice == 4:
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"Result of {num1} / {num2} is {num1/num2}")
    else:
        print("Invalid choice! Please select an option between 1 and 5.")








      
