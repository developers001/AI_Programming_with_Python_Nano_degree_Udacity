import math
#################
# Question 1
#################
class Book:
  def __init__(self, title, author, price):
    self.title = title
    self.author = author
    self.price = price

  def view(self):
    print(f'The title of the book is: {self.title}')
    print(f'The author of the book is: {self.author}')
    print(f'The price of the book is: {self.price}')

MyBook = Book('Python Course', 'Eric Matthes', '23 $')
MyBook.view()
# output: The title of the book is: Python Course
#         The author of the book is: Eric Matthes
#         The price of the book is:  23 $

#################
# Question 2
#################
class Circle:
  def __init__(self, a, b, r):
    self.a = a
    self.b = b
    self.r = r
    
  def area(self):
    return math.pi * (self.r ** 2)
  
  def perimeter(self):
    return 2 * math.pi * self.r
  
  def testBelongs(self, x, y):
    return (x-self.a)**2 + (y-self.b)**2 - self.r**2 == 0
  
class Cylinder(Circle):
  def __init__(self, a, b, r, height):
    super().__init__(a, b, r)
    self.height = height
    
  def volume(self):
    return self.area() * self.height
  
################
# Question 3
################
class BankAccount:
  def __init__(self, accountNumber, name, balance):
    self.accountNumber = accountNumber
    self.name = name
    self.balance = balance
    
  def deposit(self, deposit_amount):
    self.balance += deposit_amount
    print('Deposit success')
  
  def withdrawal(self, withdrawal_amount):
    if self.balance < withdrawal_amount:
      print(f'Insufficient funds')
    else:
      self.balance -= withdrawal_amount
      print(f'Withdrawal success')
      
  def bankFees(self):
    return self.balance * 0.95
  
  def display(self):
    print(f'Account number: {self.accountNumber}')
    print(f'Account name: {self.name}')
    print(f'Account balance: {self.balance}')