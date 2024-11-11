class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def display_info(self):
        status = "Available" if self.is_available else "Checked out"
        print(f"'{self.title}' by {self.author} - {status}")

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You checked out '{book.title}'")
                return
        print("Book not available")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"'{book.title}' has been returned")
                return
        print("Book not found")
    
    def list_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_info()
            
# Using the Library Mangement System
library = Library()

book1 = Book("One Minute Management", "Ken Blanchard")
book2 = Book("21 Indespensible Laws of Leadership", "John C Maxwell")

library.add_book(book1)
library.add_book(book2)

library.list_books()
library.checkout_book("21 Indespensible Laws of Leadership")
library.list_books()
library.return_book("21 Indespensible Laws of Leadership")
library.list_books()