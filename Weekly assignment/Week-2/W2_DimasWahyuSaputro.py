def check_type(value1, value2):
    '''
    Takes two values and returns the following:
    - If both values are integers or floats, returns the sum, multiply and percentage
    - If both values are strings, returns the concatenation and 'Other operations are not applicable'
    - If one value is string and the other is integer or float, returns the concatenation and multiplication
    '''

    # Check if both values are integers or floats
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        add = value1 + value2
        subtract = value1 - value2
        multiply = value1 * value2
        if value2 != 0: # Check if value2 is not zero
            percent = value1 / value2 * 100
            return f"{add}, {subtract}, {multiply}, {int(percent)}%"
        else:
            return "Cannot divide by zero"
        
    # Check if value 1 number and value 2 string
    elif isinstance(value1, (int, float)) and isinstance(value2, str):
        return f"{str(value1) + value2}, {value1 * value2}"
    
    # Check if value 1 string and value 2 number
    elif isinstance(value1, str) and isinstance(value2, (int, float)):
        return f"{value1 + str(value2)}, {value1 * value2}"
    
    # check if both values are strings
    else:
        return f"{str(value1)} {str(value2)}, Other operations are not applicable"


# Test cases
print(check_type(2, 3)) # 5, -1, 6, 66%
print(check_type('Hi', 'Raju')) # HiRaju, Other operations are not applicable
print(check_type(2, 'Raju')) # 2Raju, RajuRaju
