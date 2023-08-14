import math

input_values = input("Enter the input values (separated by comma): ")
input_list = input_values.split(",")

input_1 = input_list[0].strip()
input_2 = input_list[1].strip()

is_numeric_1 = input_1.isnumeric()
is_numeric_2 = input_2.isnumeric()

if is_numeric_1 and is_numeric_2:
    num_1 = int(input_1)
    num_2 = int(input_2)

    result_sum = num_1 + num_2
    result_diff = num_1 - num_2
    result_prod = num_1 * num_2
    
    if num_1 == 0 or num_2 == 0:
        result_div = 0
    else:
        result_div = math.floor(num_1 / num_2 * 100)
    
    print("{}, {}, {}, {:.0f}%".format(result_sum, result_diff, result_prod, result_div))
    
elif is_numeric_1 or is_numeric_2:

    if is_numeric_1:
        number = int(input_1)
        text = input_2
    else:
        number = int(input_2)
        text = input_1

    print("'{}', '{}'".format(input_1 + input_2, text * number))
    
else:
    print("'{} {}', 'Other operations are not applicable'".format(input_1, input_2))
