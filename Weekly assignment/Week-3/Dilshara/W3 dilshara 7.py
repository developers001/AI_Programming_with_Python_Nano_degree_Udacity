import math

def calculate_hypotenuse():
    # Get user input for the height and base of the right-angled triangle
    height = float(input("Enter the height of the right-angled triangle: "))
    base = float(input("Enter the base of the right-angled triangle: "))
    
    # Calculate the square of the height
    height_squared = height ** 2
    
    # Calculate the square of the base
    base_squared = base ** 2
    
    # Calculate the sum of the squares of height and base
    sum_of_squares = height_squared + base_squared
    
    # Calculate the square root of the sum of squares to get the length of the hypotenuse
    hypotenuse = math.sqrt(sum_of_squares)
    
    return hypotenuse
hypotenuse = calculate_hypotenuse()
print(hypotenuse)
