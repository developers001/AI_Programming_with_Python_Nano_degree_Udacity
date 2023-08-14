'''
Q1 Write a Python program/function to print the sum, largest number, 
smallest number, average of the numbers in a list.eg. [1,2,3,4,5]Sum: 15Max: 5Min: 1Mean: 3
'''

def analyze_numbers():
    input_string = input("Enter numbers separated by commas: ")
    numbers = [int(num) for num in input_string.split(",")]

    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)

    print("Sum:", total)
    print("Max:", maximum)
    print("Min:", minimum)
    print("Mean:", average)

analyze_numbers()


'''
Q2 Write a Python function that takes two lists and returns True if they have at least one common member.
eg. [“Tom”, “Bob”, “Sue”, “Rachel”],  [“Bob”, “Susan”, “Roger”, “Mike”]returns true as Bob is common
'''
def has_common_element(*lists):
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements.intersection_update(lst)
        if not common_elements:
            return False
    return True

list1 = input("Enter the elements of the first list (separated by spaces): ").split()
list2 = input("Enter the elements of the second list (separated by spaces): ").split()

# Call the function with the user-inputted lists
result = has_common_element(list1, list2)

# Print the result
if result:
    print("The two lists have at least one common element.")
else:
    print("The two lists do not have any common elements.")


'''
Q3 Write a Python program/function to combine two dictionary adding values for common keys.
eg.d1 = {'a': 100, 'b': 200, 'c':300}d2 = {'a': 300, 'b': 200, 'd':400}Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
from collections import Counter

def combine_dictionaries(d1, d2):
    result = Counter(d1)
    result.update(d2)
    return result

# Prompt the user to enter the elements of the first dictionary
dict1 = dict(input("Enter the elements of the first dictionary, key-value pairs separated by commas: ").split(",") for _ in range(int(input("Enter the number of key-value pairs for the first dictionary: "))))
dict2 = dict(input("Enter the elements of the second dictionary, key-value pairs separated by commas: ").split(",") for _ in range(int(input("Enter the number of key-value pairs for the second dictionary: "))))
result = combine_dictionaries(dict1, dict2)
print("Combined Dictionary:", result)


'''
Q4 Write a Python program/function which iterates the integers from 1 to 100. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".Sample Output :fizzbuzz12fizz4
buzz
'''
def fizz_buzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

fizz_buzz(start, end)


'''
Q5 Write a Python program/function to check the validity of password input by users.Validation :
•At least 1 letter between [a-z] and 1 letter between [A-Z].•At least 1 number between [0-9].
•At least 1 character from [$#@].•Minimum length 6 characters.•Maximum length 16 characters.
'''
def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True
    
    return has_lowercase and has_uppercase and has_digit and has_special

user_password = input("Enter your password: ")

if validate_password(user_password):
    print("Valid password.")
else:
    print("Invalid password.")


'''
Q6 Write a Python function that takes a list and returns a new list with unique elements of the first list.
 Sample List : [1,2,3,3,3,3,4,5]Unique List : [1, 2, 3, 4, 5]
'''
def get_unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = list(map(int, user_input.split()))

unique_list = get_unique_elements(input_list)
print("Unique List:", unique_list)


'''
Q7 Write a function which calculates the length of a hypotenuse of a right angle triangle given height and base.
Hint: Pythagorean theorem
'''
def calculate_hypotenuse(height, base):
    hypotenuse = (height ** 2 + base ** 2) ** 0.5
    return hypotenuse

user_height = float(input("Enter the height of the right-angled triangle: "))
user_base = float(input("Enter the base of the right-angled triangle: "))

hypotenuse = calculate_hypotenuse(user_height, user_base)
print("The length of the hypotenuse is:", hypotenuse)


'''
Q8 Scrabble score:Given a word, compute the Scrabble score for that word where the values are as followsLetter                          ValueA, E, I, O, U, L, N, R, S, T      1D, G                              2B, C, M, P                        3F,   H ,   V,   W,   Y                                          4K                                 5J, X                              8Q, Z                              10eg. “Cabbage” is worth 14 points
•3 points for C•1 point for A, twice•3 points for B, twice•2 points for G•1 point for E
'''
def scrabble_score(word):
    letter_values = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    score = 0
    for letter in word:
        score += letter_values.get(letter.upper(), 0)
    
    return score

user_word = input("Enter a word: ")
score = scrabble_score(user_word)
print("The Scrabble score for", user_word, "is", score)


'''
Q9 Write a Python program to find thegreatest common divisor(gcd) of two integers.
Hint: this is a recursive function
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = gcd(num1, num2)
print("The greatest common divisor (gcd) of", num1, "and", num2, "is", result)
