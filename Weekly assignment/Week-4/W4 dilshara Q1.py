class Book:
    def __init__(self):
        self.title = input("Enter the title of the book: ")
        self.author = input("Enter the author's name: ")
        self.price = input("Enter the price of the book: ")

    def view(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}"

# Example usage
my_book = Book()
print(my_book.view())
