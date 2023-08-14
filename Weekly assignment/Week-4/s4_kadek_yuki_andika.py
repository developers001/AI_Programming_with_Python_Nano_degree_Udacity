# -*- coding: utf-8 -*-
"""S4_Kadek Yuki Andika

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1smtYz27xpkZZ5N-sN8HlIxAAQlsXeNqs

# Question 1
"""

class Book:
  def __init__(self, title, author, price):
    self.title=title
    self. author= author
    self.price=price

  def view(self):
    print('Title: {}\nAuthor: {}\nPrice: {}'.format(self.title,self.author,self.price))

MyBook = Book('Python Course', 'Eric Matthes','23 $')
MyBook.view()

"""# Question 2"""

from math import pi

class Circle:
  def __init__(self,a,b,r):
    self.a=a
    self.b=b
    self.r=r

  def area(self):
    return pi*self.r**2

  def perimeter(self):
    return pi*2*self.r

  def testBelongs(self,x,y):
    if (x-self.a)**2 + (y-self.b)**2 - self.r**2==0:
      return True
    else:
      return False

class Cylinder(Circle):
  def __init__(self,a,b,r,height):
    Circle.__init__(self,a,b,r)
    self.height=height

  def volume(self):
    return self.area()*self.height

A = Circle(0,0,5)
print(A.area())
print(A.perimeter())
print(A.testBelongs(5,0))

B = Cylinder(0,0,5,2)
print(B.volume())

"""# Question 3"""

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees

    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)