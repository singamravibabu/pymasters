class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __add__(self, other):
        return self.pages + other.pages
    
# Creating two book objects
book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

# Using __str__() method
print(book1)    # Output: 'Python Basics' has 200 pages

# Using __add__() method
total_pages = book1 + book2
print(f"Total pages: {total_pages}")    # Output: Total pages: 500