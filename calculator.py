def calculator():
    while True:
        operation = input("'calculate' to operate or type 'quit' to exit: ")

        if operation == "quit":
            print("Calculator closed.")
            break
        else:
            num1 = float(input("Pick a number: "))
            num2 = float(input("Pick another number: "))
            operator = input("Pick operator (+, -, *, /): ")

            if operator == "+":
                print(num1 + num2)
            elif operator == "-":
                print(num1 - num2)
            elif operator == "*":
                print(num1 * num2)
            elif operator == "/":
                print(round(num1 / num2, 2))
            else:
                print("Invalid operator!")

calculator()
