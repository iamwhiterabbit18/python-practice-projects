# create a book class
class Book:
    def __init__(self, title = 'no title', author = 'no author', copies = 0):
        self.title = title
        self.author = author
        self.copies = copies
    def borrow(self):
        if self.copies <= 0:
            print(f"{self.title}: Book is not available!")
            return
        self.copies -= 1
        print(f"{self.title}: Book borrowed!")
        return self.copies
    def return_book(self):
        self.copies += 1
        print(f"{self.title}: Book returned!")
        return self.copies
    def display_details(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.copies}")

class Library:
    def __init__(self):
        self.book_list = []
    def add_book(self, book = str) -> str:
        self.book_list.append(book)
        print(f"{book.title} was added!")
    def search_book(self, book = str) -> str:
        if len(self.book_list) <= 0:
            return
        element = [x.title for x in self.book_list if x.title == book]
        if (not element):
            return "Book not found"
        return element
    def remove_book(self, book = str) -> str:
        search = [x for x in self.book_list if x.title == book]
        if search:
            self.book_list.remove(search[0])
        else:
            return "Book not found"
        return f'{search[0].title} was removed.'
    def list_books(self):
        for book in self.book_list:
            book.display_details()



    
library = Library()

book1 = Book("1984", "George Orwell", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)

library.add_book(book1)
library.add_book(book2)
library.list_books()

print(library.search_book("1984"))
print(library.search_book("The Great Gatsby"))

print(f"{book1.borrow()} copies left.")
library.list_books()

print(f"{book1.return_book()} copies left.")
library.list_books()

print(f'{library.remove_book("1984")}')
print(f'{library.remove_book("this")}')
library.list_books()
