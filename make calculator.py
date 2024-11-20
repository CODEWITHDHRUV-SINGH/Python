def number():
    # Ask for input numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Ask for the operation
    func = input("Which operation do you want to perform\t+ - * / ^: ")

    # Perform the operation and display the result
    if func == "+":
        print(num1+num2)
    elif func == "-":
        print(num1-num2)
    elif func == "*":
        print(num1*num2)
    elif func == "/":
        print(num1/num2)
    elif func == "^":
        print(num1**num2)
    else:
        print("Choose the above function only")

number()