import math


def math_on_list(lst):
    sum = 0
    maxi = lst[0]
    mini = lst[0]
    for num in lst:
        sum += num
        if num > maxi:
            maxi = num
        if num < mini:
            mini = num
    avg = sum / len(lst)
    print("The list sum is {}, maximum is {}, minimum is {}, mean is {}".format(sum, maxi, mini, avg))


def lists_intersect(lst1, lst2):
    for element1 in lst1:
        for element2 in lst2:
            if element1 == element2:
                return True
    return False


def combine_dict(dic1, dic2):
    combined = dict()
    for key in dic1:
        combined[key] = dic1[key]
    for key in dic2:
        if key in combined:
            combined[key] += dic2[key]
        else:
            combined[key] = dic2[key]
    return combined


def iterate():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def is_valid_pass(password):
    if (len(password) < 6) or (len(password) > 16):
        return False
    cnt_a = 0
    cnt_A = 0
    cnt_1 = 0
    cnt__ = 0
    for char in password:
        if char >= 'a' and (char <= 'z'):
            cnt_a += 1
        elif char >= 'A' and (char <= 'Z'):
            cnt_A += 1
        elif char >= '0' and (char <= '9'):
            cnt_1 += 1
        elif char == '@' or (char == '#') or (char == '$'):
            cnt__ += 1
    if cnt__ >= 1 and (cnt_1 >= 1) and (cnt_A >= 1) and (cnt_a >= 1):
        return True
    return False

def unique(lst):
    st = set(lst)
    return list(st)

def hypo_length(height, base):
    return math.sqrt(height*height + base*base)

def scrabble_score(word):
    dic = dict()
    dic[('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T')] = 1
    dic[('D', 'G')] = 2
    dic[('B', 'C', 'M', 'P')] = 3
    dic[('F', 'H', 'V', 'W', 'Y')] = 4
    dic[('K')] = 5
    dic[('J', 'K')] = 8
    dic[('Q', 'Z')] = 10
    score = 0
    word = word.upper()
    for char in word:
        for key in dic:
            if char in key:
                score += dic[key]
                break
    return score

def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)