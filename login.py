def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # dummy credentials
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid credentials")


if __name__ == "__main__":
    login()

for book in library.books:
    print("-", book)
library = Library()
library.add_book("self health and well being")
library.add_book("Data Structures")
library.view_books()
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'Book "{book_name}" added to the library.')

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")