def perform_operations(input1, input2):
    if isinstance(input1, (int, float)) and isinstance(input2, (int, float)):
        addition = input1 + input2
        subtraction = input1 - input2
        multiplication = input1 * input2
        percent = (input1 / input2) * 100

        return addition, subtraction, multiplication, percent
    elif not isinstance(input1, (int, float)) and not isinstance(input2, (int, float)):
        concatenation = str(input1) + str(input2)
        return concatenation
    else:
        if isinstance(input1, (int, float)):
            input1 = str(input1)
            result = input1 + str(input2)
            multiplication = int(input1) * input2
        else:
            input2 = str(input2)
            result = str(input1) + input2
            multiplication = input1 * int(input2)

        return result, multiplication
result = perform_operations(input(), input())
print(result)