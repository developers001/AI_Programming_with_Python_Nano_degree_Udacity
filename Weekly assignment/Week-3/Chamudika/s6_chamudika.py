def unique_elements(input_list):
    return list(set(input_list))

# Prompt the user to enter a list
input_list = input("Enter a list of numbers (space-separated): ").split()

# Convert the input list to integers
input_list = [int(num) for num in input_list]

# Get the unique elements
unique_list = unique_elements(input_list)

# Display the result
print("Unique List:", unique_list)
