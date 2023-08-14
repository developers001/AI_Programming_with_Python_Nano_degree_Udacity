def analyze_numbers():
    numbers = input("Enter a list of numbers (comma-separated): ").split(",")
    numbers = [float(num.strip()) for num in numbers]
    
    total = sum(numbers)
    largest = max(numbers)
    smallest = min(numbers)
    average = total / len(numbers)
    
    print("Sum:", total)
    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Average:", average)


# Call the function to analyze numbers
analyze_numbers()
