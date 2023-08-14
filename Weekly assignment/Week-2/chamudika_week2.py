def perform_operations(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        percentage = (a / b) * 100 if b != 0 else "undefined"

        print(addition)
        print(subtraction)
        print(multiplication)
        print(f"{a}/{b} = {percentage}%")

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
