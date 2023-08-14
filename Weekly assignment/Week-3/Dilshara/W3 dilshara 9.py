def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the gcd using the recursive function
result = gcd(num1, num2)

# Print the result
print("The greatest common divisor (gcd) is:", result)
