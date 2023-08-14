import math

first_input = input("Enter the first input: ")
second_input = input("Enter the second input: ")

first_is_numeric = first_input.isnumeric()
second_is_numeric = second_input.isnumeric()

if first_is_numeric and second_is_numeric:
    first = int(first_input)
    second = int(second_input)

    result_1 = first + second
    result_2 = first - second
    result_3 = first * second
    
    if first == 0 or second == 0:
        result_4 = 0
    else:
        result_4 = math.floor(first / second * 100) 
    
    print("{}, {}, {}, {:.0f}%".format(result_1, result_2, result_3, result_4))
    
elif first_is_numeric or second_is_numeric:

    if first_is_numeric:
        number = int(first_input)
        text = second_input
    else:
        number = int(second_input)
        text = first_input

    print("'{}', '{}'".format(first_input + second_input, number * text))
else:
    print("'{} {}', 'Other operations are not applicable'".format(first_input, second_input))
    
