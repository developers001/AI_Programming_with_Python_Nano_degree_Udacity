import math
import re

def question_1(list):
  print(f'Sum: {sum(list)}')
  print(f'Max: {max(list)}')
  print(f'Min: {min(list)}')
  print(f'Mean: {sum(list) / len(list)}')

def question_2(list1, list2):
  for i in list1:
    if i in list2:
      return True
  return False

def question_3(d1, d2):
  result = d2
  for key in d1:
    if key in result:
      result[key] += d1[key]
    else:
      result[key] = d1[key]
  return result

def question_4():
  for i in range(1, 101):
    if i % (3 * 5) == 0:
      print('FizzBuzz')
    elif i % 3 == 0:
      print('Fizz')
    elif i % 5 == 0:
      print('Buzz')
    else:
      print(i)

def question_5(password):
  if len(password) < 6 or len(password) > 16:
    return False
  
  if not re.search("[a-z]", password):
    return False
  if not re.search("[A-Z]", password):
    return False
  if not re.search("[0-9]", password):
    return False
  if not re.search("[$#@]", password):
    return False

  return True

def question_6(list):
  return list(set(list))

def question_7(height, base):
  hypotenuse = math.sqrt((height ** 2 + base ** 2))
  return hypotenuse

def question_8(word):
  score = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
  result = 0
  for letter in word.upper():
    result += score[letter]
  return result

def question_9(a, b):
  if b == 0:
    return a
  else:
    return question_9(b, a % b)
