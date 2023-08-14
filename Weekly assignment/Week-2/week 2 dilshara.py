def perform_operations(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
        percentage = (a / b) * 100 if b != 0 else "undefined"

        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")
        print(f"Percentage: {percentage}%")

    elif not isinstance(a, (int, float)) and not isinstance(b, (int, float)):
        concatenation = f'"{a} {b}"'
        print(concatenation)
        print("Other operations are not applicable")

    else:
        if isinstance(a,(int, float)):
            numeric = str(a)
            string = b
            
        else:
            
            string = a
            numeric = str(b)

        concatenation = f'"{numeric}{string}"'
        multiplication = f'"{string}" * 2'
        print(concatenation)
        print(eval(multiplication))

        # Check if the inputs are equal
        if a == b:
            print("The inputs are equal")
        else:
            print("The inputs are not equal")

        # Check if the inputs are both strings
        if isinstance(a, str) and isinstance(b, str):
            print("The inputs are both strings")
            print(a.upper())
            print(b.lower())

# Interactive testing
while True:
    try:
        input_1 = input("Enter the first input: ")
        input_2 = input("Enter the second input: ")

        # Check if the inputs are numeric
        if input_1.isnumeric() and input_2.isnumeric():
            input_1 = int(input_1)
            input_2 = int(input_2)
        else:
            try:
                input_1 = float(input_1)
                input_2 = float(input_2)
            except ValueError:
                pass

        # Call the function
        perform_operations(input_1, input_2)
        print()
    except KeyboardInterrupt:
        break
