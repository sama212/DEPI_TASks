import calc

flag = True

while flag:
    #ckeck operation 
    operation = input("please enter the operation name [add , sub , mult , div]: ").strip().lower()
    if operation not in ["add", "sub", "mult", "div"]:
        print("Invalid operation, please enter the operation name like [add , sub , mult , div].")
        continue
    #take numbers
    numbers = input("please enter two numbers: ").strip()
    x, y = map(int, numbers.split())
    #do operation
    if operation == "add":
        result = calc.add(x, y)
        print(f"The result of the addition is {result}")
    elif operation == "sub":
        result = calc.sub(x, y)
        print(f"The result of the subtraction is {result}")
    elif operation == "mult":
        result = calc.mult(x, y)
        print(f"The result of the multiplication is {result}")
    elif operation == "div":
        if y == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = calc.div(x, y)
        print(f"The result of the division is {result}")

    # Check if the user wants to perform another operation
    decision = calc.check()
    flag = calc.otherOperation(decision)

print("Thank you for using the calculator. Goodbye!")
