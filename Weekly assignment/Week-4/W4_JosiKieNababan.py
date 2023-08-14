# Question 1
class Book:


    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price 
    

    def view(self):
        return "Title: {}, Author: {}, Price: ${}".format(self.title, self.author, self.price)

# Uncomment below to test the Book class
# book1 = Book("Tokenisasi", "Oscar Darmawan", 3.9)
# print(book1.view())


# Question 2
class Circle:
    

    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    

    def area(self):
        return 3.14 * (self.r ** 2)
    

    def perimeter(self):
        return 2 * 3.14 * (self.r ** 2)
    

    def testBelongs(self, x, y):
        circleC = (x ** self.a) + (y-self.b) ** 2 - self.r ** 2
        if circleC == 0:
            return True
        return False
    
class Cylinder(Circle):

    
    def __init__(self, a, b, r, height):
        Circle.__init__(self, a, b, r)
        self.height = height
    
    
    def volume(self):
        return 3.14 * self.r ** 2 * self.height
    
# Uncomment below to test class in question 2
# circle1 = Circle(3,4,5)
# print(circle1.area())
# print(circle1.perimeter())
# print(circle1.testBelongs(2,3))

# cylinder1 = Cylinder(3,4,5,10)
# print(cylinder1.area())
# print(cylinder1.perimeter())
# print(cylinder1.testBelongs(2,3))
# print(cylinder1.volume())

# Question 3
class BankAccount:

    
    def __init__(self, accountNumber: int, name: str, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    

    def deposit(self, deposito):
        self.balance += deposito
    

    def withdrawal(self, totalWithdrawal):
        self.balance -= totalWithdrawal

    
    def bankFees(self):
        return self.balance * (5/100)
    

    def display(self):
        return "Account Number: {}\nName: {}\nBalance: ${}".format(self.accountNumber, self.name, self.balance)


# uncomment to test the class in Question number 3
# account1 = BankAccount(122345, "Josi Kie", 10000)
# account1.deposit(3000)
# print(account1.balance)
# account1.withdrawal(5000)
# print(account1.balance)
# print(account1.bankFees())
# print(account1.display())