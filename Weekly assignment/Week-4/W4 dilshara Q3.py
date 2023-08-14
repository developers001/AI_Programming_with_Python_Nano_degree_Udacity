class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def Withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal amount.")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print("Bank fees applied.")

    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Holder Name:", self.name)
        print("Account Balance:", self.balance)

# Test the BankAccount class
accountNumber = int(input("Enter Account Number: "))
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance: "))

bank_account = BankAccount(accountNumber, name, balance)

bank_account.display()

amount = float(input("Enter deposit amount: "))
bank_account.Deposit(amount)

amount = float(input("Enter withdrawal amount: "))
bank_account.Withdrawal(amount)

bank_account.bankFees()

bank_account.display()
