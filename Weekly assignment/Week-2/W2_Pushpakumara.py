def operations(input1, input2):
    if isinstance(input1, (int, float)) and isinstance(input2, (int, float)):
        add_result = input1 + input2
        subtract_result = input1 - input2
        multiply_result = input1 * input2
        percent_result = f"{(input1 / input2) * 100}%"
        return add_result, subtract_result, multiply_result, percent_result
    elif not isinstance(input1, (int, float)) and not isinstance(input2, (int, float)):
        concat_result = input1 + input2
        return concat_result, "Other operations are not applicable"
    else:
        if isinstance(input1, (int, float)):
            input1 = str(input1)
            concat_result = input1 + input2
            multiply_result = input1 * input2
        else:
            input2 = str(input2)
            concat_result = input1 + input2
            multiply_result = input2 * input1
        return concat_result, multiply_result
    
    
    
