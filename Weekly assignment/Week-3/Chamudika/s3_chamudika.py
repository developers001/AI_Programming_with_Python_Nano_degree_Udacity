from collections import Counter

def combine_dictionaries(dict1, dict2):
    combined_dict = Counter(dict1)
    combined_dict.update(dict2)
    return combined_dict

# Prompt the user to enter the first dictionary
dict1 = eval(input("Enter the first dictionary (in the format {'key': value, ...}): "))

# Prompt the user to enter the second dictionary
dict2 = eval(input("Enter the second dictionary (in the format {'key': value, ...}): "))

# Combine the dictionaries
combined_dict = combine_dictionaries(dict1, dict2)

# Display the result
print("Combined Dictionary:", combined_dict)
