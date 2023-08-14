def analyze_numbers(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)
    return total, maximum, minimum, average

# Prompt the user to enter a list of numbers
input_numbers = input("Enter a list of numbers (space-separated): ").split()

# Convert the input numbers to integers
numbers = [int(num) for num in input_numbers]

# Analyze the numbers
sum_numbers, max_number, min_number, avg_number = analyze_numbers(numbers)

# Display the results
print("Sum:", sum_numbers)
print("Max:", max_number)
print("Min:", min_number)
print("Mean:", avg_number)
