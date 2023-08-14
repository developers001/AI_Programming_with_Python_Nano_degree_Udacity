from collections import Counter

def combine_dictionaries():
    d1 = eval(input("Enter the first dictionary (in Python dictionary format): "))
    d2 = eval(input("Enter the second dictionary (in Python dictionary format): "))

    combined_dict = Counter(d1) + Counter(d2)
    return combined_dict


# Call the function to combine dictionaries
result = combine_dictionaries()

# Print the result
print(result)
