import math

def hypotenuse_length():
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base of the triangle: "))
    hypotenuse = math.sqrt(height ** 2 + base ** 2)
    return hypotenuse

# Example usage
print(hypotenuse_length())
