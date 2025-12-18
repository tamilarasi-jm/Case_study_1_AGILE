
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print("-", book)

library = Library()
library.add_book("Python Programming")
library.add_book("Data Structures")
library.view_books()
