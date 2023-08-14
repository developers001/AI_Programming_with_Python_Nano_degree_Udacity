def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Prompt the user to enter two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Calculate the gcd
result = gcd(num1, num2)

# Display the result
print(f"The greatest common divisor (gcd) of {num1} and {num2} is: {result}")
