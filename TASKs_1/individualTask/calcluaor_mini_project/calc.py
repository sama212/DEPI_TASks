def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def check():
    return input("do you want to do other operations [yes ,stop]: ").strip().lower()

def otherOperation(decision):
    if decision == "yes":
        return True
    elif decision == "stop":
        return False
    else:
        print("Invalid decision. Exiting the program.")
        return False
